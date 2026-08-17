-- PHASE 4: Database Schema, Storage, and RLS Policies

-- 1. Profiles Table (Maps to Supabase Auth users to handle Roles)
CREATE TABLE public.profiles (
  id UUID REFERENCES auth.users(id) ON DELETE CASCADE PRIMARY KEY,
  role TEXT CHECK (role IN ('OWNER', 'EDITOR')) NOT NULL DEFAULT 'EDITOR',
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Enable RLS on profiles
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;

-- Profiles Policies: Users can read their own profile. Owners can read all.
CREATE POLICY "Users can view own profile" 
ON public.profiles FOR SELECT USING (auth.uid() = id);

CREATE POLICY "Owners can view all profiles" 
ON public.profiles FOR SELECT USING (
  auth.uid() IN (SELECT id FROM public.profiles WHERE role = 'OWNER')
);

-- Trigger to automatically create a profile when a new auth user is created
CREATE OR REPLACE FUNCTION public.handle_new_user() 
RETURNS TRIGGER AS $$
BEGIN
  -- For the very first user, you might want to manually set them to 'OWNER' in the database.
  -- By default, we'll assign 'OWNER' for convenience so you don't get locked out initially.
  INSERT INTO public.profiles (id, role)
  VALUES (NEW.id, 'OWNER');
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();


-- 2. News & Updates Table
CREATE TABLE public.news (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  title TEXT NOT NULL,
  short_description TEXT,
  full_content TEXT,
  image_url TEXT,
  category TEXT,
  status TEXT CHECK (status IN ('DRAFT', 'PUBLISHED', 'ARCHIVED')) NOT NULL DEFAULT 'DRAFT',
  seo_title TEXT,
  seo_description TEXT,
  slug TEXT UNIQUE,
  alt_text TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  published_at TIMESTAMPTZ
);

-- Trigger to auto-update the updated_at timestamp
CREATE OR REPLACE FUNCTION handle_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_news_updated_at
  BEFORE UPDATE ON public.news
  FOR EACH ROW EXECUTE FUNCTION handle_updated_at();

-- Enable RLS on News
ALTER TABLE public.news ENABLE ROW LEVEL SECURITY;

-- News Policies
CREATE POLICY "Public can view PUBLISHED news" 
ON public.news FOR SELECT USING (status = 'PUBLISHED');

CREATE POLICY "Admins can manage news" 
ON public.news FOR ALL USING (
  auth.uid() IN (SELECT id FROM public.profiles WHERE role IN ('OWNER', 'EDITOR'))
);


-- 3. Storage Buckets & Policies
-- We insert the buckets directly (if they don't exist)
INSERT INTO storage.buckets (id, name, public, file_size_limit, allowed_mime_types) 
VALUES (
  'public_assets', 
  'public_assets', 
  true, 
  262144000, -- 250MB limit at bucket level (app-level limits will strictly enforce lower limits per file type)
  ARRAY['image/jpeg', 'image/png', 'image/webp', 'image/jpg', 'video/mp4', 'video/webm']
) ON CONFLICT (id) DO NOTHING;

INSERT INTO storage.buckets (id, name, public, file_size_limit, allowed_mime_types) 
VALUES (
  'private_assets', 
  'private_assets', 
  false, 
  26214400, -- 25MB limit for documents
  ARRAY['application/pdf']
) ON CONFLICT (id) DO NOTHING;

-- Enable RLS on storage.objects
-- (It is usually enabled by default, but we declare policies just to be sure)

-- Public Assets: Anyone can view
CREATE POLICY "Public Assets Viewable by Everyone" 
ON storage.objects FOR SELECT USING (bucket_id = 'public_assets');

-- Admins can insert/update/delete in public_assets
CREATE POLICY "Admins can manage public assets" 
ON storage.objects FOR ALL USING (
  bucket_id = 'public_assets' AND 
  auth.uid() IN (SELECT id FROM public.profiles WHERE role IN ('OWNER', 'EDITOR'))
);

-- Admins can manage private_assets
CREATE POLICY "Admins can manage private assets" 
ON storage.objects FOR ALL USING (
  bucket_id = 'private_assets' AND 
  auth.uid() IN (SELECT id FROM public.profiles WHERE role IN ('OWNER', 'EDITOR'))
);

-- Note: The Media Usage tracking requirement (warning before deletion) will be enforced via 
-- application-level logic querying the `image_url` in the `news` table before issuing a DELETE request to storage.
