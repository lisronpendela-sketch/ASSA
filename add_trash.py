import re

with open('admin/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Trash Bin Button to Dashboard
trash_btn = """
                <button id="btn-trash" class="mt-4 bg-white border border-gray-300 text-gray-800 text-xl font-bold py-5 px-12 rounded-2xl shadow hover:bg-gray-50 transition flex items-center space-x-3 w-full max-w-md justify-center">
                    <span class="text-2xl">🗑️</span>
                    <span>Trash Bin</span>
                </button>
"""
html = html.replace('<span>Media Library</span>\n                </button>', '<span>Media Library</span>\n                </button>\n' + trash_btn)


# 2. Add step-trash HTML
step_trash = """
            <!-- STEP TRASH: Trash Bin -->
            <div id="step-trash" class="w-full max-w-5xl hidden mt-6">
                <div class="flex items-center space-x-4 mb-8">
                    <button id="btn-back-trash" class="text-gray-400 hover:text-gray-800 transition"><svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg></button>
                    <h2 class="text-2xl font-bold text-gray-800">Trash Bin</h2>
                </div>
                
                <div class="bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden">
                    <div class="overflow-x-auto">
                        <table class="w-full text-left border-collapse">
                            <thead>
                                <tr class="bg-gray-50 text-gray-600 text-sm border-b border-gray-200">
                                    <th class="p-4 font-semibold">Title</th>
                                    <th class="p-4 font-semibold">Section</th>
                                    <th class="p-4 font-semibold">Deleted</th>
                                    <th class="p-4 font-semibold text-right">Actions</th>
                                </tr>
                            </thead>
                            <tbody id="trash-table-body" class="divide-y divide-gray-100">
                                <!-- Trashed Items Injected Here -->
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
"""

html = html.replace('<!-- STEP PREVIEW: Live Preview -->', step_trash + '\n            <!-- STEP PREVIEW: Live Preview -->')


# 3. Add to JS Screens
js_screens = "            stepTrash: document.getElementById('step-trash'),"
html = html.replace("stepPreview: document.getElementById('step-preview'),", "stepPreview: document.getElementById('step-preview'),\n" + js_screens)

js_hide = "            screens.stepTrash.classList.add('hidden');"
html = html.replace("screens.stepPreview.classList.add('hidden');", "screens.stepPreview.classList.add('hidden');\n" + js_hide)

js_show = "            if (viewName === 'stepTrash') screens.stepTrash.classList.remove('hidden');"
html = html.replace("if (viewName === 'stepPreview') screens.stepPreview.classList.remove('hidden');", "if (viewName === 'stepPreview') screens.stepPreview.classList.remove('hidden');\n" + js_show)


# 4. Modify window.deleteItem (Soft Delete)
old_delete = """        window.deleteItem = async function(id) {
            if (!confirm('Are you sure you want to delete this item?')) return;
            try {
                await fetch(`/api/admin/content/${currentManageSection}/${id}`, {
                    method: 'DELETE',
                    headers: { 'Authorization': 'Bearer ' + authToken }
                });
                loadManageData(currentManageSection);
            } catch(e) { alert('Error deleting item'); }
        };"""

new_delete = """        window.deleteItem = async function(id) {
            if (!confirm('Move this item to trash?')) return;
            try {
                await fetch(`/api/admin/content/${currentManageSection}/${id}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + authToken },
                    body: JSON.stringify({ status: 'TRASHED', trashed_at: new Date().toISOString() })
                });
                loadManageData(currentManageSection);
            } catch(e) { alert('Error deleting item'); }
        };"""

html = html.replace(old_delete, new_delete)

# 5. Prevent TRASHED items from appearing in normal table
old_render_table = """            data.forEach(item => {"""
new_render_table = """            data.forEach(item => {
                if (item.status === 'TRASHED') return;"""
html = html.replace(old_render_table, new_render_table)


# 6. Add Trash Logic
trash_logic = """
        document.getElementById('btn-trash').addEventListener('click', () => {
            loadTrashData();
            showView('stepTrash');
        });
        document.getElementById('btn-back-trash').addEventListener('click', () => showView('step1'));

        async function loadTrashData() {
            const tbody = document.getElementById('trash-table-body');
            tbody.innerHTML = '<tr><td colspan="4" class="p-8 text-center text-gray-500">Loading...</td></tr>';
            try {
                const res = await fetch('/api/admin/trash', { headers: { 'Authorization': 'Bearer ' + authToken } });
                const data = await res.json();
                renderTrashTable(data);
            } catch (err) {
                tbody.innerHTML = '<tr><td colspan="4" class="p-8 text-center text-red-500">Failed to load trash</td></tr>';
            }
        }

        function timeAgo(dateStr) {
            const seconds = Math.floor((new Date() - new Date(dateStr)) / 1000);
            let interval = seconds / 31536000;
            if (interval > 1) return Math.floor(interval) + " years ago";
            interval = seconds / 2592000;
            if (interval > 1) return Math.floor(interval) + " months ago";
            interval = seconds / 86400;
            if (interval > 1) return Math.floor(interval) + " days ago";
            interval = seconds / 3600;
            if (interval > 1) return Math.floor(interval) + " hours ago";
            interval = seconds / 60;
            if (interval > 1) return Math.floor(interval) + " minutes ago";
            return Math.floor(seconds) + " seconds ago";
        }

        function renderTrashTable(data) {
            const tbody = document.getElementById('trash-table-body');
            tbody.innerHTML = '';
            if (data.length === 0) {
                tbody.innerHTML = '<tr><td colspan="4" class="p-8 text-center text-gray-500">Trash is empty</td></tr>';
                return;
            }
            
            data.forEach(item => {
                const tr = document.createElement('tr');
                tr.className = 'hover:bg-gray-50 transition';
                
                tr.innerHTML = `
                    <td class="p-4 font-semibold text-gray-800">${item.title}</td>
                    <td class="p-4 text-sm text-gray-600 capitalize">${item.section}</td>
                    <td class="p-4 text-sm text-gray-500">${timeAgo(item.trashed_at || item.created_at)}</td>
                    <td class="p-4 text-right space-x-2">
                        <button onclick="restoreItem('${item.section}', '${item.id}')" class="text-blue-600 hover:text-blue-800 font-medium">Restore</button>
                        <span class="text-gray-300">|</span>
                        <button onclick="deleteItemPermanent('${item.section}', '${item.id}')" class="text-red-600 hover:text-red-800 font-medium">Delete Permanently</button>
                    </td>
                `;
                tbody.appendChild(tr);
            });
        }

        window.restoreItem = async function(section, id) {
            try {
                await fetch(`/api/admin/content/${section}/${id}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + authToken },
                    body: JSON.stringify({ status: 'DRAFT', trashed_at: null })
                });
                loadTrashData();
            } catch(e) { alert('Error restoring item'); }
        };

        window.deleteItemPermanent = async function(section, id) {
            if (!confirm('Are you sure? This cannot be undone.')) return;
            try {
                await fetch(`/api/admin/content/${section}/${id}`, {
                    method: 'DELETE',
                    headers: { 'Authorization': 'Bearer ' + authToken }
                });
                loadTrashData();
            } catch(e) { alert('Error deleting item'); }
        };
"""

html = html.replace('// Form reset logic', trash_logic + '\n        // Form reset logic')

with open('admin/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
