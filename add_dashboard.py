import re

with open('admin/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace step-1 content
old_step_1_start = '            <!-- STEP 1: Main Action -->'
old_step_1_end = '            <!-- STEP 2: Category Selection -->'

# Find the exact block
start_idx = html.find(old_step_1_start)
end_idx = html.find(old_step_1_end)

if start_idx != -1 and end_idx != -1:
    old_step_1 = html[start_idx:end_idx]
    
    new_step_1 = """            <!-- STEP 1: Main Dashboard -->
            <div id="step-1" class="w-full max-w-5xl mt-6 px-4">
                
                <!-- Greeting -->
                <div class="mb-8 flex justify-between items-end">
                    <div>
                        <h2 class="text-3xl font-bold text-gray-800" id="dash-greeting">Good afternoon, Admin 👋</h2>
                        <p class="text-gray-500 mt-1">What would you like to do today?</p>
                    </div>
                    
                    <div class="hidden md:flex space-x-3">
                        <button id="dash-btn-ai" class="bg-purple-50 text-purple-700 border border-purple-200 font-bold py-2 px-4 rounded-lg shadow-sm hover:bg-purple-100 transition flex items-center space-x-2">
                            <span>✨ Ask AI</span>
                        </button>
                        <button id="dash-btn-trash" class="bg-white text-gray-700 border border-gray-300 font-bold py-2 px-4 rounded-lg shadow-sm hover:bg-gray-50 transition flex items-center space-x-2">
                            <span>🗑️ Trash</span>
                        </button>
                    </div>
                </div>

                <!-- Quick Actions -->
                <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-10">
                    <button class="dash-quick-add bg-blue-600 text-white font-bold py-4 px-6 rounded-2xl shadow hover:bg-blue-700 hover:-translate-y-1 transition transform flex flex-col items-center justify-center text-center group" data-val="news">
                        <span class="text-3xl mb-2 group-hover:scale-110 transition">📰</span>
                        <span>+ Add News</span>
                    </button>
                    <button class="dash-quick-add bg-indigo-600 text-white font-bold py-4 px-6 rounded-2xl shadow hover:bg-indigo-700 hover:-translate-y-1 transition transform flex flex-col items-center justify-center text-center group" data-val="lectures">
                        <span class="text-3xl mb-2 group-hover:scale-110 transition">🎓</span>
                        <span>+ Add Lecture</span>
                    </button>
                    <button id="dash-btn-media" class="bg-white border border-gray-300 text-gray-800 font-bold py-4 px-6 rounded-2xl shadow hover:bg-gray-50 hover:-translate-y-1 transition transform flex flex-col items-center justify-center text-center group">
                        <span class="text-3xl mb-2 group-hover:scale-110 transition">🖼️</span>
                        <span>Media Library</span>
                    </button>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                    <!-- Website Overview (Stats) -->
                    <div class="lg:col-span-1">
                        <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-200 h-full">
                            <div class="flex justify-between items-center mb-6">
                                <h3 class="text-xl font-bold text-gray-800">Overview</h3>
                                <button id="dash-btn-manage" class="text-blue-600 text-sm font-bold hover:underline">Manage All</button>
                            </div>
                            
                            <div class="space-y-4" id="dash-overview-list">
                                <p class="text-gray-500 text-center py-4">Loading stats...</p>
                            </div>

                            <div class="mt-6 pt-6 border-t border-gray-100">
                                <div class="flex justify-between items-center bg-orange-50 p-3 rounded-lg border border-orange-100">
                                    <span class="text-orange-800 font-bold">Drafts</span>
                                    <span class="text-orange-600 font-bold text-lg" id="dash-stat-drafts">0</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Recent Activity -->
                    <div class="lg:col-span-2">
                        <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-200 h-full">
                            <h3 class="text-xl font-bold text-gray-800 mb-6">Recent Activity</h3>
                            <div class="space-y-4" id="dash-activity-list">
                                <p class="text-gray-500 py-4 text-center">Loading activity...</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Mobile extra actions -->
                <div class="mt-8 flex md:hidden flex-col space-y-3">
                    <button id="dash-btn-ai-mobile" class="bg-purple-50 text-purple-700 border border-purple-200 font-bold py-3 px-4 rounded-xl shadow-sm hover:bg-purple-100 transition text-center">
                        ✨ Ask AI Assistant
                    </button>
                    <button id="dash-btn-trash-mobile" class="bg-white text-gray-700 border border-gray-300 font-bold py-3 px-4 rounded-xl shadow-sm hover:bg-gray-50 transition text-center">
                        🗑️ Trash Bin
                    </button>
                </div>
            </div>

"""
    html = html.replace(old_step_1, new_step_1)


# Fix the loadStats JS to populate the new dashboard
old_load_stats = """        async function loadStats() {
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
        }"""

new_load_stats = """        async function loadStats() {
            try {
                // Set Greeting
                const hour = new Date().getHours();
                let greeting = 'Good evening';
                if (hour < 12) greeting = 'Good morning';
                else if (hour < 18) greeting = 'Good afternoon';
                document.getElementById('dash-greeting').textContent = `${greeting}, Admin 👋`;

                const res = await fetch('/api/admin/stats', {
                    headers: { 'Authorization': 'Bearer ' + authToken }
                });
                const data = await res.json();
                
                // Populate Overview
                document.getElementById('dash-stat-drafts').textContent = data.stats.drafts || 0;
                
                const overviewList = document.getElementById('dash-overview-list');
                overviewList.innerHTML = '';
                
                const labels = {
                    news: 'Published News',
                    lectures: 'Free Lectures',
                    courses: 'Courses',
                    gallery: 'Gallery Items',
                    testimonials: 'Testimonials',
                    announcements: 'Announcements'
                };

                let hasStats = false;
                for (const [section, count] of Object.entries(data.sectionCounts || {})) {
                    if (count > 0) {
                        hasStats = true;
                        overviewList.innerHTML += `
                            <div class="flex justify-between items-center">
                                <span class="text-gray-700 font-medium">${labels[section] || section}</span>
                                <span class="text-gray-900 font-bold bg-gray-100 px-3 py-1 rounded-full">${count}</span>
                            </div>
                        `;
                    }
                }
                if (!hasStats) overviewList.innerHTML = '<p class="text-gray-500 text-sm">No published content yet.</p>';

                // Populate Activity
                const activityList = document.getElementById('dash-activity-list');
                activityList.innerHTML = '';
                
                if (!data.recentActivity || data.recentActivity.length === 0) {
                    activityList.innerHTML = '<p class="text-gray-500 text-sm">No recent activity.</p>';
                } else {
                    data.recentActivity.forEach(act => {
                        const timeStr = timeAgo(act.date);
                        activityList.innerHTML += `
                            <div class="flex items-start space-x-3">
                                <div class="mt-1 w-6 h-6 rounded-full bg-blue-100 text-blue-600 flex items-center justify-center flex-shrink-0">
                                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                                </div>
                                <div>
                                    <p class="text-gray-800 text-sm font-medium">${act.message}</p>
                                    <p class="text-gray-400 text-xs mt-0.5">${timeStr}</p>
                                </div>
                            </div>
                        `;
                    });
                }
            } catch (err) {
                console.warn('Could not load stats');
            }
        }
        
        function setupDashboardLinks() {
            // Quick Add
            document.querySelectorAll('.dash-quick-add').forEach(btn => {
                btn.addEventListener('click', () => {
                    const val = btn.getAttribute('data-val');
                    const name = val === 'news' ? 'News & Update' : 'Free Lecture';
                    document.getElementById('entry-section').value = val;
                    document.getElementById('selected-cat-name').textContent = name;
                    resetForm();
                    document.getElementById('add-form').removeAttribute('data-edit-id');
                    showView('step3');
                });
            });

            // Re-bind old button IDs to new dashboard IDs
            const bindClick = (id, targetView, action) => {
                const el = document.getElementById(id);
                if (el) el.addEventListener('click', () => {
                    if (action) action();
                    showView(targetView);
                });
            };
            
            bindClick('dash-btn-ai', 'stepAi');
            bindClick('dash-btn-ai-mobile', 'stepAi');
            bindClick('dash-btn-trash', 'stepTrash', loadTrashData);
            bindClick('dash-btn-trash-mobile', 'stepTrash', loadTrashData);
            bindClick('dash-btn-media', 'stepMedia', loadMediaLibrary);
            bindClick('dash-btn-manage', 'stepManageCats');
        }
        
        // Call setupDashboardLinks once on load
        setTimeout(setupDashboardLinks, 100);
"""

html = html.replace(old_load_stats, new_load_stats)

with open('admin/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
