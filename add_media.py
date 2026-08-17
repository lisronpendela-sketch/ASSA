import re

with open('admin/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add "Media Library" button to step-1
media_btn = """
                <button id="btn-media" class="mt-4 bg-white border border-gray-300 text-gray-800 text-xl font-bold py-5 px-12 rounded-2xl shadow hover:bg-gray-50 transition flex items-center space-x-3 w-full max-w-md justify-center">
                    <span class="text-2xl">🖼️</span>
                    <span>Media Library</span>
                </button>
"""
html = html.replace('<span>Manage Content</span>\n                </button>', '<span>Manage Content</span>\n                </button>\n' + media_btn)

# 2. Add step-media HTML
step_media = """
            <!-- STEP MEDIA: Media Library -->
            <div id="step-media" class="w-full max-w-5xl hidden mt-6">
                <div class="flex items-center justify-between mb-8">
                    <div class="flex items-center space-x-4">
                        <button id="btn-back-media" class="text-gray-400 hover:text-gray-800 transition"><svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg></button>
                        <h2 class="text-2xl font-bold text-gray-800">Media Library</h2>
                    </div>
                    
                    <label class="bg-blue-600 text-white font-bold py-2 px-4 rounded-lg shadow hover:bg-blue-700 transition flex items-center space-x-2 cursor-pointer">
                        <span>+ Upload</span>
                        <input type="file" id="media-direct-upload" class="hidden">
                    </label>
                </div>
                
                <div class="bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden p-6">
                    <div class="flex flex-col md:flex-row justify-between items-center mb-6 space-y-4 md:space-y-0">
                        <input type="text" id="media-search" placeholder="Search files..." class="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 w-full md:w-64">
                        <div class="flex space-x-2">
                            <button class="media-filter px-4 py-2 bg-blue-50 text-blue-700 rounded-lg font-medium border border-blue-200" data-type="all">All</button>
                            <button class="media-filter px-4 py-2 hover:bg-gray-50 text-gray-700 rounded-lg font-medium border border-transparent" data-type="image">Images</button>
                            <button class="media-filter px-4 py-2 hover:bg-gray-50 text-gray-700 rounded-lg font-medium border border-transparent" data-type="video">Videos</button>
                            <button class="media-filter px-4 py-2 hover:bg-gray-50 text-gray-700 rounded-lg font-medium border border-transparent" data-type="pdf">PDFs</button>
                        </div>
                    </div>
                    
                    <div id="media-grid" class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 gap-4">
                        <!-- Media items injected here -->
                    </div>
                </div>
            </div>

            <!-- Media Modal -->
            <div id="media-modal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center hidden z-50">
                <div class="bg-white rounded-2xl shadow-xl w-full max-w-md p-6 relative">
                    <button onclick="document.getElementById('media-modal').classList.add('hidden')" class="absolute top-4 right-4 text-gray-400 hover:text-gray-800">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                    </button>
                    <h3 class="text-xl font-bold mb-4">File Information</h3>
                    <div class="space-y-3 text-sm text-gray-700 mb-6">
                        <p><span class="font-bold">Name:</span> <span id="modal-file-name" class="break-all"></span></p>
                        <p><span class="font-bold">Size:</span> <span id="modal-file-size"></span></p>
                        <p><span class="font-bold">Uploaded:</span> <span id="modal-file-date"></span></p>
                        <p><span class="font-bold">Usage:</span> <span id="modal-file-usage" class="text-blue-600 font-bold bg-blue-50 px-2 py-1 rounded"></span></p>
                    </div>
                    <div class="flex space-x-3">
                        <button id="modal-btn-copy" class="flex-1 py-2 px-4 border border-gray-300 rounded-lg font-bold text-gray-700 hover:bg-gray-50">Copy Link</button>
                        <button id="modal-btn-delete" class="flex-1 py-2 px-4 bg-red-600 rounded-lg font-bold text-white hover:bg-red-700">Delete</button>
                    </div>
                </div>
            </div>
"""

html = html.replace('<!-- STEP 3: Form Entry -->', step_media + '\n            <!-- STEP 3: Form Entry -->')

# 3. JS Additions
js_screens = "            stepMedia: document.getElementById('step-media'),"
html = html.replace("stepManageList: document.getElementById('step-manage-list'),", "stepManageList: document.getElementById('step-manage-list'),\n" + js_screens)

js_hide = "            screens.stepMedia.classList.add('hidden');"
html = html.replace("screens.stepManageList.classList.add('hidden');", "screens.stepManageList.classList.add('hidden');\n" + js_hide)

js_show = "            if (viewName === 'stepMedia') screens.stepMedia.classList.remove('hidden');"
html = html.replace("if (viewName === 'stepManageList') screens.stepManageList.classList.remove('hidden');", "if (viewName === 'stepManageList') screens.stepManageList.classList.remove('hidden');\n" + js_show)

js_logic = """
        document.getElementById('btn-media').addEventListener('click', () => {
            loadMediaLibrary();
            showView('stepMedia');
        });
        document.getElementById('btn-back-media').addEventListener('click', () => showView('step1'));

        window.currentMediaData = [];
        window.currentMediaFilter = 'all';

        async function loadMediaLibrary() {
            const grid = document.getElementById('media-grid');
            grid.innerHTML = '<p class="col-span-full text-center text-gray-500 py-8">Loading media...</p>';
            try {
                const res = await fetch('/api/admin/media', {
                    headers: { 'Authorization': 'Bearer ' + authToken }
                });
                const data = await res.json();
                window.currentMediaData = data;
                renderMediaGrid();
            } catch(e) {
                grid.innerHTML = '<p class="col-span-full text-center text-red-500 py-8">Failed to load media</p>';
            }
        }

        function formatBytes(bytes, decimals = 2) {
            if (!+bytes) return '0 Bytes';
            const k = 1024;
            const dm = decimals < 0 ? 0 : decimals;
            const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
            const i = Math.floor(Math.log(bytes) / Math.log(k));
            return `${parseFloat((bytes / Math.pow(k, i)).toFixed(dm))} ${sizes[i]}`;
        }

        function renderMediaGrid() {
            const grid = document.getElementById('media-grid');
            const q = document.getElementById('media-search').value.toLowerCase();
            grid.innerHTML = '';
            
            let filtered = window.currentMediaData.filter(m => m.name.toLowerCase().includes(q));
            
            if (window.currentMediaFilter !== 'all') {
                filtered = filtered.filter(m => {
                    const ext = m.name.split('.').pop().toLowerCase();
                    if (window.currentMediaFilter === 'image') return ['jpg','jpeg','png','gif','webp'].includes(ext);
                    if (window.currentMediaFilter === 'video') return ['mp4','avi','mov','mkv'].includes(ext);
                    if (window.currentMediaFilter === 'pdf') return ['pdf'].includes(ext);
                    return true;
                });
            }

            if (filtered.length === 0) {
                grid.innerHTML = '<p class="col-span-full text-center text-gray-500 py-8">No files found</p>';
                return;
            }

            filtered.forEach(file => {
                const div = document.createElement('div');
                div.className = 'border border-gray-200 rounded-xl overflow-hidden shadow-sm hover:shadow-md cursor-pointer transition group';
                div.onclick = () => openMediaModal(file);
                
                const ext = file.name.split('.').pop().toLowerCase();
                const isImage = ['jpg','jpeg','png','gif','webp'].includes(ext);
                
                let preview = `<div class="w-full h-32 bg-gray-100 flex items-center justify-center text-4xl group-hover:scale-105 transition transform">📄</div>`;
                if (isImage) {
                    preview = `<img src="${file.url}" class="w-full h-32 object-cover group-hover:scale-105 transition transform">`;
                } else if (['mp4','avi','mov','mkv'].includes(ext)) {
                    preview = `<div class="w-full h-32 bg-gray-900 flex items-center justify-center text-4xl group-hover:scale-105 transition transform text-white">▶️</div>`;
                }
                
                div.innerHTML = `
                    <div class="overflow-hidden bg-gray-100">${preview}</div>
                    <div class="p-3">
                        <p class="text-xs font-semibold text-gray-800 truncate" title="${file.name}">${file.name}</p>
                        <p class="text-xs text-gray-500">${formatBytes(file.size)}</p>
                    </div>
                `;
                grid.appendChild(div);
            });
        }

        document.getElementById('media-search').addEventListener('input', renderMediaGrid);
        
        document.querySelectorAll('.media-filter').forEach(btn => {
            btn.addEventListener('click', (e) => {
                document.querySelectorAll('.media-filter').forEach(b => {
                    b.classList.remove('bg-blue-50', 'text-blue-700', 'border-blue-200');
                    b.classList.add('text-gray-700', 'border-transparent');
                });
                e.target.classList.remove('text-gray-700', 'border-transparent');
                e.target.classList.add('bg-blue-50', 'text-blue-700', 'border-blue-200');
                window.currentMediaFilter = e.target.getAttribute('data-type');
                renderMediaGrid();
            });
        });

        function openMediaModal(file) {
            document.getElementById('modal-file-name').textContent = file.name;
            document.getElementById('modal-file-size').textContent = formatBytes(file.size);
            document.getElementById('modal-file-date').textContent = new Date(file.created_at).toLocaleDateString();
            document.getElementById('modal-file-usage').textContent = `Used in ${file.used_count} places`;
            
            const btnCopy = document.getElementById('modal-btn-copy');
            btnCopy.onclick = () => {
                navigator.clipboard.writeText(window.location.origin + file.url);
                btnCopy.textContent = 'Copied!';
                setTimeout(() => btnCopy.textContent = 'Copy Link', 2000);
            };

            const btnDelete = document.getElementById('modal-btn-delete');
            if (file.used_count > 0) {
                btnDelete.classList.add('opacity-50', 'cursor-not-allowed');
                btnDelete.onclick = () => alert(`Cannot delete. This file is currently used in ${file.used_count} places.`);
            } else {
                btnDelete.classList.remove('opacity-50', 'cursor-not-allowed');
                btnDelete.onclick = async () => {
                    if (!confirm('Are you sure you want to delete this file?')) return;
                    try {
                        const res = await fetch(`/api/admin/media/${file.name}`, {
                            method: 'DELETE',
                            headers: { 'Authorization': 'Bearer ' + authToken }
                        });
                        const data = await res.json();
                        if (data.success) {
                            document.getElementById('media-modal').classList.add('hidden');
                            loadMediaLibrary();
                        } else {
                            alert(data.error);
                        }
                    } catch(err) {
                        alert('Delete failed');
                    }
                };
            }
            
            document.getElementById('media-modal').classList.remove('hidden');
        }

        document.getElementById('media-direct-upload').addEventListener('change', async (e) => {
            if (e.target.files.length === 0) return;
            const file = e.target.files[0];
            try {
                // Show a quick visual indication
                e.target.parentElement.innerHTML = '<span>Uploading...</span>';
                const url = await uploadFile(file);
                // Reset input
                e.target.parentElement.innerHTML = '<span>+ Upload</span><input type="file" id="media-direct-upload" class="hidden">';
                // Reattach listener since we replaced HTML
                document.getElementById('media-direct-upload').addEventListener('change', arguments.callee);
                loadMediaLibrary();
            } catch(err) {
                alert('Upload failed: ' + err.message);
                e.target.parentElement.innerHTML = '<span>+ Upload</span><input type="file" id="media-direct-upload" class="hidden">';
                document.getElementById('media-direct-upload').addEventListener('change', arguments.callee);
            }
        });
"""
html = html.replace('document.getElementById(\'btn-manage\').addEventListener(\'click\', () => showView(\'stepManageCats\'));', js_logic + '\n        document.getElementById(\'btn-manage\').addEventListener(\'click\', () => showView(\'stepManageCats\'));')

with open('admin/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
