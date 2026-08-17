@echo off
cd /d "%~dp0"
echo Starting Custom Node.js Admin Server...
echo Do not close this window while testing your website.
start http://localhost:8000/admin/index.html
start http://localhost:8000/
node server.js
