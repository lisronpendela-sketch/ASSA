import re

with open('admin/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update STEP-2 Cards
step2_start = '<!-- Category Cards -->'
step2_end = '</div>\n            </div>\n\n            <!-- STEP AI: Smart Input -->'

new_step2_cards = """<!-- Category Cards -->
                    <button class="cat-card bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:border-blue-500 hover:shadow-md transition text-left group" data-val="news">
                        <div class="text-4xl mb-4 group-hover:scale-110 transition transform origin-left">📰</div>
                        <h3 class="text-lg font-bold text-gray-800">News</h3>
                    </button>
                    <button class="cat-card bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:border-blue-500 hover:shadow-md transition text-left group" data-val="lectures">
                        <div class="text-4xl mb-4 group-hover:scale-110 transition transform origin-left">🎓</div>
                        <h3 class="text-lg font-bold text-gray-800">Free Lectures</h3>
                    </button>
                    <button class="cat-card bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:border-blue-500 hover:shadow-md transition text-left group" data-val="courses">
                        <div class="text-4xl mb-4 group-hover:scale-110 transition transform origin-left">📚</div>
                        <h3 class="text-lg font-bold text-gray-800">Courses</h3>
                    </button>
                    <button class="cat-card bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:border-blue-500 hover:shadow-md transition text-left group" data-val="classes">
                        <div class="text-4xl mb-4 group-hover:scale-110 transition transform origin-left">🏫</div>
                        <h3 class="text-lg font-bold text-gray-800">Classes</h3>
                    </button>
                    <button class="cat-card bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:border-blue-500 hover:shadow-md transition text-left group" data-val="achievements">
                        <div class="text-4xl mb-4 group-hover:scale-110 transition transform origin-left">🏆</div>
                        <h3 class="text-lg font-bold text-gray-800">Achievements</h3>
                    </button>
                    <button class="cat-card bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:border-blue-500 hover:shadow-md transition text-left group" data-val="books">
                        <div class="text-4xl mb-4 group-hover:scale-110 transition transform origin-left">📖</div>
                        <h3 class="text-lg font-bold text-gray-800">Books</h3>
                    </button>
                    <button class="cat-card bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:border-blue-500 hover:shadow-md transition text-left group" data-val="tests">
                        <div class="text-4xl mb-4 group-hover:scale-110 transition transform origin-left">📝</div>
                        <h3 class="text-lg font-bold text-gray-800">Tests</h3>
                    </button>
                    <button class="cat-card bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:border-blue-500 hover:shadow-md transition text-left group" data-val="about">
                        <div class="text-4xl mb-4 group-hover:scale-110 transition transform origin-left">ℹ️</div>
                        <h3 class="text-lg font-bold text-gray-800">About</h3>
                    </button>
                    <button class="cat-card bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:border-blue-500 hover:shadow-md transition text-left group" data-val="contact">
                        <div class="text-4xl mb-4 group-hover:scale-110 transition transform origin-left">📞</div>
                        <h3 class="text-lg font-bold text-gray-800">Contact</h3>
                    </button>
"""
import re
html = re.sub(r'<!-- Category Cards -->.*?</div>\s+</div>\s+<!-- STEP AI: Smart Input -->', new_step2_cards + '                </div>\n            </div>\n\n            <!-- STEP AI: Smart Input -->', html, flags=re.DOTALL)


# 2. Update STEP-MANAGE-CATS Cards
manage_start = '<!-- STEP MANAGE CATS: Category Selection for Management -->'
manage_end = '<!-- STEP MANAGE LIST: Table view -->'
new_manage_cards = """<!-- STEP MANAGE CATS: Category Selection for Management -->
            <div id="step-manage-cats" class="w-full max-w-4xl hidden mt-6">
                <div class="flex items-center space-x-4 mb-6">
                    <button id="btn-back-manage-cats" class="text-gray-400 hover:text-gray-800 transition"><svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg></button>
                    <h2 class="text-2xl font-bold text-gray-800">Which section do you want to manage?</h2>
                </div>
                
                <div class="grid grid-cols-2 md:grid-cols-3 gap-4 sm:gap-6">
                    <button class="manage-cat-card bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:border-blue-500 hover:shadow-md transition text-left group" data-val="news">
                        <div class="text-4xl mb-4 group-hover:scale-110 transition transform origin-left">📰</div>
                        <h3 class="text-lg font-bold text-gray-800">News</h3>
                    </button>
                    <button class="manage-cat-card bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:border-blue-500 hover:shadow-md transition text-left group" data-val="lectures">
                        <div class="text-4xl mb-4 group-hover:scale-110 transition transform origin-left">🎓</div>
                        <h3 class="text-lg font-bold text-gray-800">Free Lectures</h3>
                    </button>
                    <button class="manage-cat-card bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:border-blue-500 hover:shadow-md transition text-left group" data-val="courses">
                        <div class="text-4xl mb-4 group-hover:scale-110 transition transform origin-left">📚</div>
                        <h3 class="text-lg font-bold text-gray-800">Courses</h3>
                    </button>
                    <button class="manage-cat-card bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:border-blue-500 hover:shadow-md transition text-left group" data-val="classes">
                        <div class="text-4xl mb-4 group-hover:scale-110 transition transform origin-left">🏫</div>
                        <h3 class="text-lg font-bold text-gray-800">Classes</h3>
                    </button>
                    <button class="manage-cat-card bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:border-blue-500 hover:shadow-md transition text-left group" data-val="achievements">
                        <div class="text-4xl mb-4 group-hover:scale-110 transition transform origin-left">🏆</div>
                        <h3 class="text-lg font-bold text-gray-800">Achievements</h3>
                    </button>
                    <button class="manage-cat-card bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:border-blue-500 hover:shadow-md transition text-left group" data-val="books">
                        <div class="text-4xl mb-4 group-hover:scale-110 transition transform origin-left">📖</div>
                        <h3 class="text-lg font-bold text-gray-800">Books</h3>
                    </button>
                    <button class="manage-cat-card bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:border-blue-500 hover:shadow-md transition text-left group" data-val="tests">
                        <div class="text-4xl mb-4 group-hover:scale-110 transition transform origin-left">📝</div>
                        <h3 class="text-lg font-bold text-gray-800">Tests</h3>
                    </button>
                    <button class="manage-cat-card bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:border-blue-500 hover:shadow-md transition text-left group" data-val="about">
                        <div class="text-4xl mb-4 group-hover:scale-110 transition transform origin-left">ℹ️</div>
                        <h3 class="text-lg font-bold text-gray-800">About</h3>
                    </button>
                    <button class="manage-cat-card bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:border-blue-500 hover:shadow-md transition text-left group" data-val="contact">
                        <div class="text-4xl mb-4 group-hover:scale-110 transition transform origin-left">📞</div>
                        <h3 class="text-lg font-bold text-gray-800">Contact</h3>
                    </button>
                </div>
            </div>

            """
html = re.sub(r'<!-- STEP MANAGE CATS: Category Selection for Management -->.*?<!-- STEP MANAGE LIST: Table view -->', new_manage_cards + '<!-- STEP MANAGE LIST: Table view -->', html, flags=re.DOTALL)

# 3. Update loadStats mapping
old_labels = """                const labels = {
                    news: 'Published News',
                    lectures: 'Free Lectures',
                    courses: 'Courses',
                    gallery: 'Gallery Items',
                    testimonials: 'Testimonials',
                    announcements: 'Announcements'
                };"""
new_labels = """                const labels = {
                    news: 'News',
                    lectures: 'Free Lectures',
                    courses: 'Courses',
                    classes: 'Classes',
                    achievements: 'Achievements',
                    books: 'Books',
                    tests: 'Tests',
                    about: 'About',
                    contact: 'Contact'
                };"""
html = html.replace(old_labels, new_labels)

# 4. Update AI Parser Mapping
old_ai_detect = """            // Detect Section
            if (prompt.includes('lecture') || prompt.includes('video')) { section = 'lectures'; sectionName = 'Free Lecture'; }
            else if (prompt.includes('course')) { section = 'courses'; sectionName = 'Course'; }
            else if (prompt.includes('gallery') || prompt.includes('photo') || prompt.includes('picture')) { section = 'gallery'; sectionName = 'Gallery'; }
            else if (prompt.includes('testimonial') || prompt.includes('review')) { section = 'testimonials'; sectionName = 'Testimonial'; }
            else if (prompt.includes('announcement')) { section = 'announcements'; sectionName = 'Announcement'; }"""

new_ai_detect = """            // Detect Section
            if (prompt.includes('lecture') || prompt.includes('video')) { section = 'lectures'; sectionName = 'Free Lectures'; }
            else if (prompt.includes('course')) { section = 'courses'; sectionName = 'Courses'; }
            else if (prompt.includes('class')) { section = 'classes'; sectionName = 'Classes'; }
            else if (prompt.includes('achieve') || prompt.includes('award')) { section = 'achievements'; sectionName = 'Achievements'; }
            else if (prompt.includes('book')) { section = 'books'; sectionName = 'Books'; }
            else if (prompt.includes('test') || prompt.includes('exam')) { section = 'tests'; sectionName = 'Tests'; }
            else if (prompt.includes('about')) { section = 'about'; sectionName = 'About'; }
            else if (prompt.includes('contact')) { section = 'contact'; sectionName = 'Contact'; }"""
html = html.replace(old_ai_detect, new_ai_detect)


with open('admin/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
