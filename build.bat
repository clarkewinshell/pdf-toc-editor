@echo off
pip install pyinstaller
pip install -r requirements.txt
pyinstaller --onefile --noconsole --windowed --name pdf-toc-editor --icon assets/icon.ico --strip --upx-dir "C:/upx" --exclude-module tkinter --exclude-module PyQt5.QtWebEngineWidgets app/main.py
