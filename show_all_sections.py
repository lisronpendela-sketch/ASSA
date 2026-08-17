import re

with open('admin/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

dashboard_actions_start = '<h3 class="text-lg font-bold text-gray-800 mb-4">Or choose an action</h3>'
dashboard_actions_end = '<!-- Dashboard Bottom Grid -->'

new_actions_html = """<h3 class="text-lg font-bold text-gray-800 mb-4">Quick Add & Manage</h3>
                    <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
                        <button class="dash-quick-add bg-white border border-gray-300 text-gray-800 font-bold py-3 px-4 rounded-xl shadow hover:bg-blue-50 hover:border-blue-300 hover:-translate-y-1 transition transform flex flex-col items-center justify-center text-center group" data-val="news" data-name="News">
                            <span class="text-2xl mb-1 group-hover:scale-110 transition">📰</span>
                            <span class="text-sm">News</span>
                        </button>
                        
                        <button class="dash-quick-add bg-white border border-gray-300 text-gray-800 font-bold py-3 px-4 rounded-xl shadow hover:bg-blue-50 hover:border-blue-300 hover:-translate-y-1 transition transform flex flex-col items-center justify-center text-center group" data-val="lectures" data-name="Free Lectures">
                            <span class="text-2xl mb-1 group-hover:scale-110 transition">🎓</span>
                            <span class="text-sm">Lectures</span>
                        </button>
                        
                        <button class="dash-quick-add bg-white border border-gray-300 text-gray-800 font-bold py-3 px-4 rounded-xl shadow hover:bg-blue-50 hover:border-blue-300 hover:-translate-y-1 transition transform flex flex-col items-center justify-center text-center group" data-val="courses" data-name="Courses">
                            <span class="text-2xl mb-1 group-hover:scale-110 transition">📚</span>
                            <span class="text-sm">Courses</span>
                        </button>
                        
                        <button class="dash-quick-add bg-white border border-gray-300 text-gray-800 font-bold py-3 px-4 rounded-xl shadow hover:bg-blue-50 hover:border-blue-300 hover:-translate-y-1 transition transform flex flex-col items-center justify-center text-center group" data-val="classes" data-name="Classes">
                            <span class="text-2xl mb-1 group-hover:scale-110 transition">🏫</span>
                            <span class="text-sm">Classes</span>
                        </button>
                        
                        <button class="dash-quick-add bg-white border border-gray-300 text-gray-800 font-bold py-3 px-4 rounded-xl shadow hover:bg-blue-50 hover:border-blue-300 hover:-translate-y-1 transition transform flex flex-col items-center justify-center text-center group" data-val="achievements" data-name="Achievements">
                            <span class="text-2xl mb-1 group-hover:scale-110 transition">🏆</span>
                            <span class="text-sm">Achieve</span>
                        </button>
                        
                        <button class="dash-quick-add bg-white border border-gray-300 text-gray-800 font-bold py-3 px-4 rounded-xl shadow hover:bg-blue-50 hover:border-blue-300 hover:-translate-y-1 transition transform flex flex-col items-center justify-center text-center group" data-val="books" data-name="Books">
                            <span class="text-2xl mb-1 group-hover:scale-110 transition">📖</span>
                            <span class="text-sm">Books</span>
                        </button>
                        
                        <button class="dash-quick-add bg-white border border-gray-300 text-gray-800 font-bold py-3 px-4 rounded-xl shadow hover:bg-blue-50 hover:border-blue-300 hover:-translate-y-1 transition transform flex flex-col items-center justify-center text-center group" data-val="tests" data-name="Tests">
                            <span class="text-2xl mb-1 group-hover:scale-110 transition">📝</span>
                            <span class="text-sm">Tests</span>
                        </button>
                        
                        <button class="dash-quick-add bg-white border border-gray-300 text-gray-800 font-bold py-3 px-4 rounded-xl shadow hover:bg-blue-50 hover:border-blue-300 hover:-translate-y-1 transition transform flex flex-col items-center justify-center text-center group" data-val="about" data-name="About">
                            <span class="text-2xl mb-1 group-hover:scale-110 transition">ℹ️</span>
                            <span class="text-sm">About</span>
                        </button>
                        
                        <button class="dash-quick-add bg-white border border-gray-300 text-gray-800 font-bold py-3 px-4 rounded-xl shadow hover:bg-blue-50 hover:border-blue-300 hover:-translate-y-1 transition transform flex flex-col items-center justify-center text-center group" data-val="contact" data-name="Contact">
                            <span class="text-2xl mb-1 group-hover:scale-110 transition">📞</span>
                            <span class="text-sm">Contact</span>
                        </button>

                        <button id="dash-btn-media" class="bg-white border border-gray-300 text-gray-800 font-bold py-3 px-4 rounded-xl shadow hover:bg-gray-50 hover:-translate-y-1 transition transform flex flex-col items-center justify-center text-center group">
                            <span class="text-2xl mb-1 group-hover:scale-110 transition">🖼️</span>
                            <span class="text-sm">Media</span>
                        </button>

                        <button id="dash-btn-manage" class="col-span-2 md:col-span-2 lg:col-span-2 bg-gradient-to-r from-blue-600 to-indigo-600 text-white font-bold py-3 px-4 rounded-xl shadow hover:shadow-lg hover:-translate-y-1 transition transform flex items-center justify-center space-x-2 group">
                            <svg class="w-6 h-6 group-hover:rotate-12 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
                            <span>Manage Content</span>
                        </button>
                    </div>
                </div>
                
                <!-- Dashboard Bottom Grid -->"""

html = re.sub(r'<h3 class="text-lg font-bold text-gray-800 mb-4">Or choose an action</h3>.*?<!-- Dashboard Bottom Grid -->', new_actions_html, html, flags=re.DOTALL)


# Update setupDashboardLinks to use the dynamic data-name attribute we just added
setup_links_old = """            // Quick Add
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
            });"""

setup_links_new = """            // Quick Add
            document.querySelectorAll('.dash-quick-add').forEach(btn => {
                btn.addEventListener('click', () => {
                    const val = btn.getAttribute('data-val');
                    const name = btn.getAttribute('data-name');
                    document.getElementById('entry-section').value = val;
                    document.getElementById('selected-cat-name').textContent = name;
                    resetForm();
                    document.getElementById('add-form').removeAttribute('data-edit-id');
                    showView('step3');
                });
            });"""
html = html.replace(setup_links_old, setup_links_new)

with open('admin/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
