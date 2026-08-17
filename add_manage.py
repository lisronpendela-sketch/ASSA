import re

with open('admin/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

manage_cats_html = """
            <!-- STEP MANAGE CATS: Category Selection for Management -->
            <div id="step-manage-cats" class="w-full max-w-4xl hidden mt-6">
                <div class="flex items-center space-x-4 mb-6">
                    <button id="btn-back-manage-cats" class="text-gray-400 hover:text-gray-800 transition"><svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg></button>
                    <h2 class="text-2xl font-bold text-gray-800">Which section do you want to manage?</h2>
                </div>
                
                <div class="grid grid-cols-2 md:grid-cols-3 gap-4 sm:gap-6">
                    <button class="manage-cat-card bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:border-blue-500 hover:shadow-md transition text-left group" data-val="news">
                        <div class="text-4xl mb-4 group-hover:scale-110 transition transform origin-left">📰</div>
                        <h3 class="text-lg font-bold text-gray-800">News & Update</h3>
                    </button>
                    <button class="manage-cat-card bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:border-blue-500 hover:shadow-md transition text-left group" data-val="lectures">
                        <div class="text-4xl mb-4 group-hover:scale-110 transition transform origin-left">🎓</div>
                        <h3 class="text-lg font-bold text-gray-800">Free Lecture</h3>
                    </button>
                    <button class="manage-cat-card bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:border-blue-500 hover:shadow-md transition text-left group" data-val="courses">
                        <div class="text-4xl mb-4 group-hover:scale-110 transition transform origin-left">📚</div>
                        <h3 class="text-lg font-bold text-gray-800">Course</h3>
                    </button>
                    <button class="manage-cat-card bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:border-blue-500 hover:shadow-md transition text-left group" data-val="gallery">
                        <div class="text-4xl mb-4 group-hover:scale-110 transition transform origin-left">🖼️</div>
                        <h3 class="text-lg font-bold text-gray-800">Gallery</h3>
                    </button>
                    <button class="manage-cat-card bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:border-blue-500 hover:shadow-md transition text-left group" data-val="testimonials">
                        <div class="text-4xl mb-4 group-hover:scale-110 transition transform origin-left">⭐</div>
                        <h3 class="text-lg font-bold text-gray-800">Testimonial</h3>
                    </button>
                    <button class="manage-cat-card bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:border-blue-500 hover:shadow-md transition text-left group" data-val="announcements">
                        <div class="text-4xl mb-4 group-hover:scale-110 transition transform origin-left">📢</div>
                        <h3 class="text-lg font-bold text-gray-800">Announcement</h3>
                    </button>
                </div>
            </div>

            <!-- STEP MANAGE LIST: Table view -->
            <div id="step-manage-list" class="w-full max-w-5xl hidden mt-6">
                <div class="flex items-center justify-between mb-8">
                    <div class="flex items-center space-x-4">
                        <button id="btn-back-manage-list" class="text-gray-400 hover:text-gray-800 transition"><svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg></button>
                        <h2 class="text-2xl font-bold text-gray-800"><span id="manage-list-title">Content</span></h2>
                    </div>
                    <button id="btn-manage-add-new" class="bg-blue-600 text-white font-bold py-2 px-4 rounded-lg shadow hover:bg-blue-700 transition flex items-center space-x-2">
                        <span>+ Add New</span>
                    </button>
                </div>
                
                <div class="bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden">
                    <div class="p-4 border-b border-gray-200 flex justify-between items-center bg-gray-50">
                        <input type="text" id="manage-search" placeholder="Search..." class="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 w-64">
                    </div>
                    <div class="overflow-x-auto">
                        <table class="w-full text-left border-collapse">
                            <thead>
                                <tr class="bg-gray-50 text-gray-600 text-sm border-b border-gray-200">
                                    <th class="p-4 font-semibold">Thumbnail</th>
                                    <th class="p-4 font-semibold">Title</th>
                                    <th class="p-4 font-semibold">Status</th>
                                    <th class="p-4 font-semibold">Date</th>
                                    <th class="p-4 font-semibold text-right">Actions</th>
                                </tr>
                            </thead>
                            <tbody id="manage-table-body" class="divide-y divide-gray-100">
                                <!-- Dynamic Rows -->
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
"""

html = html.replace('<!-- STEP 3: Form Entry -->', manage_cats_html + '\n            <!-- STEP 3: Form Entry -->')

js_additions = """
            stepManageCats: document.getElementById('step-manage-cats'),
            stepManageList: document.getElementById('step-manage-list'),
"""

html = html.replace("stepAi: document.getElementById('step-ai')", "stepAi: document.getElementById('step-ai'),\n" + js_additions)

js_hide_additions = """
            screens.stepManageCats.classList.add('hidden');
            screens.stepManageList.classList.add('hidden');
"""

html = html.replace("screens.stepAi.classList.add('hidden');", "screens.stepAi.classList.add('hidden');\n" + js_hide_additions)

js_show_additions = """
            if (viewName === 'stepManageCats') screens.stepManageCats.classList.remove('hidden');
            if (viewName === 'stepManageList') screens.stepManageList.classList.remove('hidden');
"""

html = html.replace("if (viewName === 'stepAi') screens.stepAi.classList.remove('hidden');", "if (viewName === 'stepAi') screens.stepAi.classList.remove('hidden');\n" + js_show_additions)

js_logic = """
        document.getElementById('btn-manage').addEventListener('click', () => showView('stepManageCats'));
        document.getElementById('btn-back-manage-cats').addEventListener('click', () => showView('step1'));
        document.getElementById('btn-back-manage-list').addEventListener('click', () => showView('stepManageCats'));
        
        let currentManageSection = '';
        
        document.querySelectorAll('.manage-cat-card').forEach(card => {
            card.addEventListener('click', () => {
                const val = card.getAttribute('data-val');
                const name = card.querySelector('h3').textContent;
                currentManageSection = val;
                document.getElementById('manage-list-title').textContent = name;
                document.getElementById('entry-section').value = val;
                document.getElementById('selected-cat-name').textContent = name;
                loadManageData(val);
                showView('stepManageList');
            });
        });

        document.getElementById('btn-manage-add-new').addEventListener('click', () => {
            resetForm();
            document.getElementById('add-form').removeAttribute('data-edit-id');
            showView('step3');
        });

        async function loadManageData(section) {
            const tbody = document.getElementById('manage-table-body');
            tbody.innerHTML = '<tr><td colspan="5" class="p-8 text-center text-gray-500">Loading...</td></tr>';
            try {
                const res = await fetch(`/api/admin/content/${section}`, {
                    headers: { 'Authorization': 'Bearer ' + authToken }
                });
                const data = await res.json();
                window.currentManageData = data;
                renderManageTable(data);
            } catch (err) {
                tbody.innerHTML = '<tr><td colspan="5" class="p-8 text-center text-red-500">Failed to load data</td></tr>';
            }
        }

        function renderManageTable(data) {
            const tbody = document.getElementById('manage-table-body');
            tbody.innerHTML = '';
            if (data.length === 0) {
                tbody.innerHTML = '<tr><td colspan="5" class="p-8 text-center text-gray-500">No content found</td></tr>';
                return;
            }
            
            data.forEach(item => {
                const tr = document.createElement('tr');
                tr.className = 'hover:bg-gray-50 transition';
                
                let thumbHtml = '<div class="w-12 h-12 bg-gray-200 rounded flex items-center justify-center text-gray-400">📄</div>';
                const imgUrl = item.thumbnail_url || (item.file_url && item.file_url.match(/\.(jpeg|jpg|gif|png)$/i) ? item.file_url : null);
                if (imgUrl) {
                    thumbHtml = `<img src="${imgUrl}" class="w-12 h-12 object-cover rounded shadow-sm">`;
                }

                const statusColor = item.status === 'PUBLISHED' ? 'text-green-600 bg-green-50' : 'text-orange-600 bg-orange-50';
                
                tr.innerHTML = `
                    <td class="p-4">${thumbHtml}</td>
                    <td class="p-4 font-semibold text-gray-800">${item.title}</td>
                    <td class="p-4">
                        <span class="px-3 py-1 rounded-full text-xs font-bold ${statusColor}">${item.status || 'PUBLISHED'}</span>
                    </td>
                    <td class="p-4 text-gray-500 text-sm">${item.date || '-'}</td>
                    <td class="p-4 text-right space-x-2">
                        <button onclick="editItem('${item.id}')" class="text-blue-600 hover:text-blue-800 font-medium">Edit</button>
                        <span class="text-gray-300">|</span>
                        <button onclick="toggleStatus('${item.id}')" class="text-gray-600 hover:text-gray-800 font-medium">${item.status === 'DRAFT' ? 'Publish' : 'Unpublish'}</button>
                        <span class="text-gray-300">|</span>
                        <button onclick="deleteItem('${item.id}')" class="text-red-600 hover:text-red-800 font-medium">Delete</button>
                    </td>
                `;
                tbody.appendChild(tr);
            });
        }
        
        document.getElementById('manage-search').addEventListener('input', (e) => {
            const q = e.target.value.toLowerCase();
            if (!window.currentManageData) return;
            const filtered = window.currentManageData.filter(i => i.title.toLowerCase().includes(q));
            renderManageTable(filtered);
        });

        window.editItem = function(id) {
            const item = window.currentManageData.find(i => i.id === id);
            if (!item) return;
            resetForm();
            document.getElementById('entry-title').value = item.title || '';
            document.getElementById('entry-desc').value = item.description || '';
            if (item.category) document.getElementById('entry-category').value = item.category;
            if (item.date) document.getElementById('entry-date').value = item.date;
            
            const radios = document.getElementsByName('status');
            for (let i = 0; i < radios.length; i++) {
                if (radios[i].value === (item.status || 'PUBLISHED')) radios[i].checked = true;
            }
            
            document.getElementById('add-form').setAttribute('data-edit-id', id);
            showView('step3');
        };

        window.toggleStatus = async function(id) {
            const item = window.currentManageData.find(i => i.id === id);
            if (!item) return;
            const newStatus = item.status === 'DRAFT' ? 'PUBLISHED' : 'DRAFT';
            
            try {
                await fetch(`/api/admin/content/${currentManageSection}/${id}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + authToken },
                    body: JSON.stringify({ status: newStatus })
                });
                loadManageData(currentManageSection);
            } catch(e) { alert('Error updating status'); }
        };

        window.deleteItem = async function(id) {
            if (!confirm('Are you sure you want to delete this item?')) return;
            try {
                await fetch(`/api/admin/content/${currentManageSection}/${id}`, {
                    method: 'DELETE',
                    headers: { 'Authorization': 'Bearer ' + authToken }
                });
                loadManageData(currentManageSection);
            } catch(e) { alert('Error deleting item'); }
        };
"""

html = html.replace('// Form reset logic', js_logic + '\n        // Form reset logic')

with open('admin/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
