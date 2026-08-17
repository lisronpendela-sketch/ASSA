require('dotenv').config();
const express = require('express');
const cors = require('cors');
const multer = require('multer');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 8000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static files from current directory
app.use(express.static(path.join(__dirname)));
app.use('/uploads', express.static(path.join(__dirname, 'uploads')));

// File upload setup using multer
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        const uploadDir = path.join(__dirname, 'uploads');
        if (!fs.existsSync(uploadDir)) {
            fs.mkdirSync(uploadDir);
        }
        cb(null, uploadDir);
    },
    filename: (req, file, cb) => {
        cb(null, Date.now() + '-' + file.originalname.replace(/\s+/g, '-'));
    }
});
const upload = multer({ 
    storage, 
    limits: { fileSize: 250 * 1024 * 1024 } // 250MB limit
});

// Admin Credentials from Environment Variables
const ADMIN_EMAIL = process.env.ADMIN_EMAIL;
const ADMIN_PASS = process.env.ADMIN_PASS;

// Simple Data Store (JSON file)
const DATA_FILE = path.join(__dirname, 'data.json');

// Helper to read data
function readData() {
    if (!fs.existsSync(DATA_FILE)) {
        const defaultData = { news: [] };
        fs.writeFileSync(DATA_FILE, JSON.stringify(defaultData, null, 2));
        return defaultData;
    }
    const raw = fs.readFileSync(DATA_FILE);
    return JSON.parse(raw);
}

// Helper to write data
function writeData(data) {
    fs.writeFileSync(DATA_FILE, JSON.stringify(data, null, 2));
}

// Authentication Middleware
function requireAuth(req, res, next) {
    // A simple implementation checking headers for a token
    const token = req.headers.authorization;
    if (token === 'Bearer ' + Buffer.from(`${ADMIN_EMAIL}:${ADMIN_PASS}`).toString('base64')) {
        next();
    } else {
        res.status(401).json({ error: 'Unauthorized' });
    }
}

// Routes
app.post('/api/login', (req, res) => {
    const { email, password } = req.body;
    if (email === ADMIN_EMAIL && password === ADMIN_PASS) {
        const token = Buffer.from(`${ADMIN_EMAIL}:${ADMIN_PASS}`).toString('base64');
        res.json({ success: true, token });
    } else {
        res.status(401).json({ error: 'Invalid credentials' });
    }
});

app.get('/api/news', (req, res) => {
    const data = readData();
    // Return only published news for public endpoint
    const published = data.news.filter(n => n.status === 'PUBLISHED');
    res.json(published);
});

// Admin routes
app.post('/api/admin/content', requireAuth, (req, res) => {
    const data = readData();
    const section = req.body.section; // courses, lectures, books, news
    
    if (!data[section]) {
        data[section] = [];
    }
    
    const newItem = {
        id: Date.now().toString(),
        title: req.body.title,
        description: req.body.description,
        file_url: req.body.file_url,
        thumbnail_url: req.body.thumbnail_url,
        category: req.body.category,
        date: req.body.date,
        status: req.body.status || 'PUBLISHED',
        created_at: new Date().toISOString()
    };
    
    // Add to top of array
    data[section].unshift(newItem);
    // Activity log
    let titleStr = req.body.title ? `"${req.body.title}"` : 'an item';
    if (req.body.status === 'PUBLISHED') logActivity(`Published new ${section} item: ${titleStr}`);
    else logActivity(`Saved draft for ${section} item: ${titleStr}`);

    writeData(data);
    
    res.json({ success: true, item: newItem });
});

app.get('/api/content/:section', (req, res) => {
    const data = readData();
    const section = req.params.section;
    const items = data[section] || [];
    // Only return items that are explicitly PUBLISHED, or have no status (legacy)
    const publishedItems = items.filter(i => i.status === 'PUBLISHED' || !i.status);
    res.json(publishedItems);
});

// --- NEW ADMIN CRUD ROUTES ---

// Get Global Stats & Activity
app.get('/api/admin/stats', requireAuth, (req, res) => {
    const data = readData();
    let stats = { drafts: 0, published: 0, archived: 0, trashed: 0 };
    let sectionCounts = {};
    
    Object.keys(data).forEach(section => {
        if (section === 'activityLog') return; // skip activity log
        
        if (Array.isArray(data[section])) {
            sectionCounts[section] = 0;
            data[section].forEach(item => {
                if (item.status === 'DRAFT') stats.drafts++;
                else if (item.status === 'ARCHIVED') stats.archived++;
                else if (item.status === 'TRASHED') stats.trashed++;
                else {
                    stats.published++; // PUBLISHED or missing status
                    sectionCounts[section]++; // Only count published for the overview
                }
            });
        }
    });
    
    // Sort activity log
    const activity = data.activityLog || [];
    activity.sort((a, b) => new Date(b.date) - new Date(a.date));
    
    res.json({
        stats,
        sectionCounts,
        recentActivity: activity.slice(0, 5) // top 5
    });
});

// Helper function to log activity
function logActivity(message) {
    const data = readData();
    if (!data.activityLog) data.activityLog = [];
    data.activityLog.push({
        message,
        date: new Date().toISOString()
    });
    // keep only last 50
    if (data.activityLog.length > 50) data.activityLog.shift();
    writeData(data);
}

// Get ALL Trashed Items
app.get('/api/admin/trash', requireAuth, (req, res) => {
    const data = readData();
    let trashList = [];
    Object.keys(data).forEach(section => {
        if (Array.isArray(data[section])) {
            data[section].forEach(item => {
                if (item.status === 'TRASHED') {
                    trashList.push({ ...item, section }); // Add section so frontend knows where it belongs
                }
            });
        }
    });
    trashList.sort((a, b) => new Date(b.trashed_at || b.created_at) - new Date(a.trashed_at || a.created_at));
    res.json(trashList);
});

// Get ALL content for a section (including drafts)
app.get('/api/admin/content/:section', requireAuth, (req, res) => {
    const data = readData();
    const section = req.params.section;
    res.json(data[section] || []);
});

// Update content
app.put('/api/admin/content/:section/:id', requireAuth, (req, res) => {
    const data = readData();
    const { section, id } = req.params;
    
    if (!data[section]) return res.status(404).json({ error: 'Section not found' });
    
    const index = data[section].findIndex(item => item.id === id);
    if (index === -1) return res.status(404).json({ error: 'Item not found' });
    
    // Update fields
    const currentItem = data[section][index];
    data[section][index] = {
        ...currentItem,
        title: req.body.title !== undefined ? req.body.title : currentItem.title,
        description: req.body.description !== undefined ? req.body.description : currentItem.description,
        category: req.body.category !== undefined ? req.body.category : currentItem.category,
        date: req.body.date !== undefined ? req.body.date : currentItem.date,
        status: req.body.status !== undefined ? req.body.status : currentItem.status,
        file_url: req.body.file_url !== undefined ? req.body.file_url : currentItem.file_url,
        thumbnail_url: req.body.thumbnail_url !== undefined ? req.body.thumbnail_url : currentItem.thumbnail_url,
        trashed_at: req.body.trashed_at !== undefined ? req.body.trashed_at : currentItem.trashed_at
    };
    
    const titleStr = currentItem.title ? `"${currentItem.title}"` : 'an item';
    if (req.body.status === 'TRASHED') logActivity(`Moved ${section} item to trash: ${titleStr}`);
    else logActivity(`Updated ${section} item: ${titleStr}`);

    writeData(data);
    res.json({ success: true, item: data[section][index] });
});

// Delete content
app.delete('/api/admin/content/:section/:id', requireAuth, (req, res) => {
    const data = readData();
    const { section, id } = req.params;
    
    if (!data[section]) return res.status(404).json({ error: 'Section not found' });
    
    const deletedItem = data[section].find(item => item.id === id);
    const titleStr = deletedItem && deletedItem.title ? `"${deletedItem.title}"` : 'an item';
    
    const initialLength = data[section].length;
    data[section] = data[section].filter(item => item.id !== id);
    
    if (data[section].length === initialLength) {
        return res.status(404).json({ error: 'Item not found' });
    }
    
    logActivity(`Permanently deleted ${section} item: ${titleStr}`);
    writeData(data);
    res.json({ success: true });
});

// -----------------------------

// File upload
app.post('/api/admin/upload', requireAuth, upload.single('media'), (req, res) => {
    if (!req.file) return res.status(400).json({ error: 'No file uploaded' });
    logActivity(`Uploaded a new file: ${req.file.filename}`);
    res.json({ success: true, url: `/uploads/${req.file.filename}`, filename: req.file.filename });
});

app.get('/api/admin/media', requireAuth, (req, res) => {
    const uploadDir = path.join(__dirname, 'uploads');
    if (!fs.existsSync(uploadDir)) return res.json([]);
    
    const data = readData();
    
    const files = fs.readdirSync(uploadDir).map(name => {
        const stats = fs.statSync(path.join(uploadDir, name));
        
        // Calculate usage
        let usedCount = 0;
        Object.values(data).forEach(sectionArray => {
            if (Array.isArray(sectionArray)) {
                sectionArray.forEach(item => {
                    if ((item.file_url && item.file_url.includes(name)) || 
                        (item.thumbnail_url && item.thumbnail_url.includes(name))) {
                        usedCount++;
                    }
                });
            }
        });

        return {
            name,
            url: `/uploads/${name}`,
            size: stats.size,
            created_at: stats.birthtime,
            used_count: usedCount
        };
    });
    // Sort newest first
    files.sort((a, b) => b.created_at - a.created_at);
    res.json(files);
});

app.delete('/api/admin/media/:filename', requireAuth, (req, res) => {
    const filename = req.params.filename;
    if (filename.includes('..') || filename.includes('/')) {
        return res.status(400).json({ error: 'Invalid filename' });
    }
    
    // Check if in use
    const data = readData();
    let usedCount = 0;
    Object.values(data).forEach(sectionArray => {
        if (Array.isArray(sectionArray)) {
            sectionArray.forEach(item => {
                if ((item.file_url && item.file_url.includes(filename)) || 
                    (item.thumbnail_url && item.thumbnail_url.includes(filename))) {
                    usedCount++;
                }
            });
        }
    });

    if (usedCount > 0) {
        return res.status(400).json({ error: `Cannot delete. File is currently used in ${usedCount} pieces of content.` });
    }
    
    const filepath = path.join(__dirname, 'uploads', filename);
    if (fs.existsSync(filepath)) {
        fs.unlinkSync(filepath);
        res.json({ success: true });
    } else {
        res.status(404).json({ error: 'File not found' });
    }
});

// Fallback to route /admin to /admin/index.html
app.get('/admin', (req, res) => {
    res.sendFile(path.join(__dirname, 'admin', 'index.html'));
});

app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
