import re

with open('admin/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Inject the AI Bar into Step 1
ai_bar = """
                <!-- Premium AI Feature -->
                <div class="bg-gradient-to-r from-purple-50 to-indigo-50 border border-purple-200 rounded-2xl p-6 mb-10 shadow-sm relative overflow-hidden">
                    <div class="absolute -top-10 -right-10 text-purple-200 opacity-50 transform rotate-12">
                        <svg class="w-48 h-48" fill="currentColor" viewBox="0 0 20 20"><path d="M10 2a8 8 0 100 16 8 8 0 000-16zm0 14a6 6 0 110-12 6 6 0 010 12zm0-10a1 1 0 00-1 1v3a1 1 0 002 0V7a1 1 0 00-1-1z"></path></svg>
                    </div>
                    
                    <div class="relative z-10">
                        <h3 class="text-xl font-bold text-purple-900 mb-2 flex items-center space-x-2">
                            <span>✨</span>
                            <span>What would you like to do?</span>
                        </h3>
                        <div class="flex space-x-4 mt-4">
                            <input type="text" id="ai-prompt-dash" class="flex-1 px-4 py-4 rounded-xl border border-purple-200 focus:ring-2 focus:ring-purple-500 focus:border-purple-500 text-lg shadow-sm" placeholder="e.g., Add a new free lecture about calculus...">
                            <button id="btn-parse-ai-dash" class="bg-purple-600 text-white font-bold py-4 px-8 rounded-xl shadow-lg hover:bg-purple-700 hover:-translate-y-1 transition transform whitespace-nowrap">
                                Tell Assistant
                            </button>
                        </div>
                    </div>
                </div>

                <div class="flex items-center space-x-4 mb-6">
                    <div class="h-px bg-gray-200 flex-1"></div>
                    <span class="text-gray-400 font-medium text-sm uppercase tracking-wider">Or choose an action</span>
                    <div class="h-px bg-gray-200 flex-1"></div>
                </div>
"""

# Insert it right before <!-- Quick Actions -->
html = html.replace('<!-- Quick Actions -->', ai_bar + '\n                <!-- Quick Actions -->')

# 2. Hide or remove the old AI button from the Greeting area
html = html.replace('''<button id="dash-btn-ai" class="bg-purple-50 text-purple-700 border border-purple-200 font-bold py-2 px-4 rounded-lg shadow-sm hover:bg-purple-100 transition flex items-center space-x-2">
                            <span>✨ Ask AI</span>
                        </button>''', '')

html = html.replace('''<button id="dash-btn-ai-mobile" class="bg-purple-50 text-purple-700 border border-purple-200 font-bold py-3 px-4 rounded-xl shadow-sm hover:bg-purple-100 transition text-center">
                        ✨ Ask AI Assistant
                    </button>''', '')


# 3. Modify JS AI Parser to use the new dashboard input
old_ai_js = """        document.getElementById('btn-parse-ai').addEventListener('click', () => {
            const prompt = document.getElementById('ai-prompt').value.toLowerCase();"""

new_ai_js = """        document.getElementById('btn-parse-ai-dash').addEventListener('click', () => {
            const prompt = document.getElementById('ai-prompt-dash').value.toLowerCase();"""

html = html.replace(old_ai_js, new_ai_js)

# We can also handle 'Enter' key on the new input
enter_key_js = """
        document.getElementById('ai-prompt-dash').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') document.getElementById('btn-parse-ai-dash').click();
        });
"""

html = html.replace("const prompt = document.getElementById('ai-prompt-dash').value.toLowerCase();", "const prompt = document.getElementById('ai-prompt-dash').value.toLowerCase();" + enter_key_js)

with open('admin/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
