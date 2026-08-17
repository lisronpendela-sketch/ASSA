import re

with open('admin/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Statistics block to Step 1
stats_html = """
            <!-- STEP 1: Main Action -->
            <div id="step-1" class="w-full max-w-3xl flex flex-col items-center mt-10">
                <div class="text-center mb-10">
                    <h2 class="text-3xl font-bold text-gray-800 mb-2">Welcome Back!</h2>
                    <p class="text-gray-500 mb-6">What would you like to do today?</p>
                    
                    <div class="flex justify-center space-x-6 bg-white p-4 rounded-xl shadow-sm border border-gray-200 w-full max-w-md mx-auto mb-8">
                        <div class="text-center">
                            <div class="text-2xl font-bold text-orange-500" id="stat-drafts">-</div>
                            <div class="text-xs font-bold text-gray-500 uppercase tracking-wide">Drafts</div>
                        </div>
                        <div class="w-px bg-gray-200"></div>
                        <div class="text-center">
                            <div class="text-2xl font-bold text-green-600" id="stat-published">-</div>
                            <div class="text-xs font-bold text-gray-500 uppercase tracking-wide">Published</div>
                        </div>
                        <div class="w-px bg-gray-200"></div>
                        <div class="text-center">
                            <div class="text-2xl font-bold text-gray-600" id="stat-archived">-</div>
                            <div class="text-xs font-bold text-gray-500 uppercase tracking-wide">Archived</div>
                        </div>
                    </div>
                </div>
"""
html = html.replace('''            <!-- STEP 1: Main Action -->
            <div id="step-1" class="w-full max-w-3xl flex flex-col items-center mt-10">
                <div class="text-center mb-10">
                    <h2 class="text-3xl font-bold text-gray-800 mb-2">Welcome Back!</h2>
                    <p class="text-gray-500">What would you like to do today?</p>
                </div>''', stats_html)

# 2. Add Archived Radio Button & Preview Button
radio_html = """
                                        <label class="flex items-center space-x-2 cursor-pointer">
                                            <input type="radio" name="status" value="PUBLISHED" class="w-5 h-5 text-blue-600" checked>
                                            <span class="text-gray-700 font-medium">Published</span>
                                        </label>
                                        <label class="flex items-center space-x-2 cursor-pointer">
                                            <input type="radio" name="status" value="ARCHIVED" class="w-5 h-5 text-gray-600">
                                            <span class="text-gray-700 font-medium">Archived</span>
                                        </label>
"""
html = html.replace('''                                        <label class="flex items-center space-x-2 cursor-pointer">
                                            <input type="radio" name="status" value="PUBLISHED" class="w-5 h-5 text-blue-600" checked>
                                            <span class="text-gray-700 font-medium">Published</span>
                                        </label>''', radio_html)

preview_html = """
                        <div class="flex justify-end space-x-4 pt-4 border-t border-gray-100 mt-6">
                            <button type="button" class="px-6 py-3 rounded-xl border border-gray-300 text-gray-700 font-bold hover:bg-gray-50 transition" onclick="submitForm('DRAFT', true)">Preview</button>
                            <button type="button" class="px-6 py-3 rounded-xl border border-gray-300 text-gray-700 font-bold hover:bg-gray-50 transition" onclick="submitForm('DRAFT')">Save Draft</button>
"""
html = html.replace('''                        <div class="flex justify-end space-x-4 pt-4 border-t border-gray-100 mt-6">
                            <button type="button" class="px-6 py-3 rounded-xl border border-gray-300 text-gray-700 font-bold hover:bg-gray-50 transition" onclick="alert('Preview mode opening soon')">Preview</button>
                            <button type="button" class="px-6 py-3 rounded-xl border border-gray-300 text-gray-700 font-bold hover:bg-gray-50 transition" onclick="submitForm('DRAFT')">Save Draft</button>''', preview_html)

# 3. Update loadStats logic
js_stats = """
        async function loadStats() {
            try {
                const res = await fetch('/api/admin/stats', {
                    headers: { 'Authorization': 'Bearer ' + authToken }
                });
                const data = await res.json();
                document.getElementById('stat-drafts').textContent = data.drafts || 0;
                document.getElementById('stat-published').textContent = data.published || 0;
                document.getElementById('stat-archived').textContent = data.archived || 0;
            } catch (err) {
                console.warn('Could not load stats');
            }
        }

        function showView(viewName) {
"""
html = html.replace('''        function showView(viewName) {''', js_stats)

js_showview = """            if (viewName === 'step1') {
                screens.step1.classList.remove('hidden');
                loadStats();
            }"""
html = html.replace("if (viewName === 'step1') screens.step1.classList.remove('hidden');", js_showview)

# 4. Update submitForm for Preview
submit_func = """
        // Submission Logic
        async function submitForm(statusValue, isPreview = false) {
"""
html = html.replace('''        // Submission Logic
        async function submitForm(statusValue) {''', submit_func)

submit_success = """
                progress.classList.add('hidden');
                successEl.textContent = status === 'DRAFT' ? '📝 Saved as Draft successfully!' : '🎉 Published! The item is now live.';
                if (isPreview) successEl.textContent = 'Opening Preview...';
                successEl.classList.remove('hidden');
                
                setTimeout(() => {
                    if (isPreview) {
                        window.open('/', '_blank');
                    }
                    if (editId) {
                        loadManageData(section);
                        showView('stepManageList');
                    } else {
                        showView('step1');
                    }
                }, 1500);
"""

# Replace the timeout part of the submit logic
old_timeout = """                progress.classList.add('hidden');
                successEl.textContent = status === 'DRAFT' ? '📝 Saved as Draft successfully!' : '🎉 Published! The item is now live.';
                successEl.classList.remove('hidden');
                
                setTimeout(() => {
                    if (editId) {
                        loadManageData(section);
                        showView('stepManageList');
                    } else {
                        showView('step1');
                    }
                }, 2000);"""

html = html.replace(old_timeout, submit_success)


# Fix status color in manage table for ARCHIVED
old_status_color = "const statusColor = item.status === 'PUBLISHED' ? 'text-green-600 bg-green-50' : 'text-orange-600 bg-orange-50';"
new_status_color = "const statusColor = item.status === 'PUBLISHED' ? 'text-green-600 bg-green-50' : (item.status === 'ARCHIVED' ? 'text-gray-600 bg-gray-100' : 'text-orange-600 bg-orange-50');"
html = html.replace(old_status_color, new_status_color)

with open('admin/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
