import re

with open('admin/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

modals_html = """
    <!-- NEWS MODAL -->
    <div id="modal-news" class="fixed inset-0 z-50 flex items-center justify-center bg-gray-900 bg-opacity-50 hidden">
        <div class="bg-white p-6 rounded-lg shadow-xl w-full max-w-2xl max-h-[90vh] overflow-y-auto">
            <div class="flex justify-between items-center mb-4">
                <h3 class="text-xl font-bold" id="news-modal-title">Create News Article</h3>
                <button class="text-gray-500 hover:text-gray-800" onclick="document.getElementById('modal-news').classList.add('hidden')">✕</button>
            </div>
            <form id="form-news" class="space-y-4">
                <input type="hidden" id="news-id">
                
                <div>
                    <label class="block text-sm font-medium">Title</label>
                    <input type="text" id="news-title" required class="mt-1 w-full border border-gray-300 rounded px-3 py-2">
                </div>
                
                <div>
                    <label class="block text-sm font-medium">Category</label>
                    <input type="text" id="news-category" class="mt-1 w-full border border-gray-300 rounded px-3 py-2" placeholder="e.g. Announcement, Event">
                </div>

                <div>
                    <label class="block text-sm font-medium">Cover Image URL (Or use Media Library)</label>
                    <div class="flex gap-2">
                        <input type="url" id="news-image" class="mt-1 flex-1 border border-gray-300 rounded px-3 py-2" placeholder="https://...">
                        <button type="button" class="mt-1 bg-gray-200 px-4 py-2 rounded text-sm hover:bg-gray-300" onclick="alert('Media picker coming soon')">Browse</button>
                    </div>
                </div>

                <div>
                    <label class="block text-sm font-medium">Short Description</label>
                    <textarea id="news-short" rows="2" class="mt-1 w-full border border-gray-300 rounded px-3 py-2"></textarea>
                </div>

                <div>
                    <label class="block text-sm font-medium">Full Content</label>
                    <textarea id="news-content" rows="4" class="mt-1 w-full border border-gray-300 rounded px-3 py-2"></textarea>
                </div>

                <div class="flex items-center gap-4 border-t pt-4">
                    <label class="flex items-center gap-2">
                        <input type="radio" name="news-status" value="DRAFT" checked>
                        <span>Draft</span>
                    </label>
                    <label class="flex items-center gap-2">
                        <input type="radio" name="news-status" value="PUBLISHED">
                        <span>Published</span>
                    </label>
                </div>

                <div class="flex justify-end gap-3 pt-2">
                    <button type="button" class="px-4 py-2 text-gray-600 bg-gray-100 hover:bg-gray-200 rounded" onclick="document.getElementById('modal-news').classList.add('hidden')">Cancel</button>
                    <button type="submit" class="px-4 py-2 text-white bg-blue-600 hover:bg-blue-700 rounded flex items-center">
                        <span id="news-btn-text">Save Article</span>
                        <div class="loader ml-2 hidden" id="news-spinner"></div>
                    </button>
                </div>
            </form>
        </div>
    </div>

    <!-- MEDIA UPLOAD MODAL -->
    <div id="modal-media" class="fixed inset-0 z-50 flex items-center justify-center bg-gray-900 bg-opacity-50 hidden">
        <div class="bg-white p-6 rounded-lg shadow-xl w-full max-w-md">
            <div class="flex justify-between items-center mb-4">
                <h3 class="text-xl font-bold">Upload Media</h3>
                <button class="text-gray-500 hover:text-gray-800" onclick="document.getElementById('modal-media').classList.add('hidden')">✕</button>
            </div>
            <form id="form-media" class="space-y-4">
                <div>
                    <label class="block text-sm font-medium mb-1">Select File</label>
                    <input type="file" id="media-file" required class="w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100">
                    <p class="text-xs text-gray-500 mt-2">Max limits: Image 10MB, Video 250MB, PDF 25MB.</p>
                </div>

                <div id="upload-progress-container" class="hidden">
                    <div class="w-full bg-gray-200 rounded-full h-2 mt-2">
                        <div class="bg-blue-600 h-2 rounded-full" id="upload-progress-bar" style="width: 0%"></div>
                    </div>
                    <p class="text-xs text-center mt-1" id="upload-progress-text">0%</p>
                </div>

                <div id="media-error" class="text-red-500 text-sm hidden"></div>

                <div class="flex justify-end gap-3 pt-4 border-t">
                    <button type="button" class="px-4 py-2 text-gray-600 bg-gray-100 hover:bg-gray-200 rounded" onclick="document.getElementById('modal-media').classList.add('hidden')">Cancel</button>
                    <button type="submit" class="px-4 py-2 text-white bg-blue-600 hover:bg-blue-700 rounded" id="media-upload-btn">Upload</button>
                </div>
            </form>
        </div>
    </div>
"""

# Insert modals right before the Supabase script tag
html = html.replace('<!-- Include Supabase JS Client via CDN -->', modals_html + '\n    <!-- Include Supabase JS Client via CDN -->')

with open('admin/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Modals added to index.html")
