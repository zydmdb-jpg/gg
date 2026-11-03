@echo off
chcp 65001 >nul
title نظام إدارة ديون المولدة - ماهر
cd /d "%~dp0"

echo ========================================================
echo       جاري تشغيل نظام إدارة ديون ومشتركي المولدة
echo ========================================================

:: Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo تم العثور على بايثون، جاري تشغيل السيرفر وفتح الموقع...
    python server.py
) else (
    echo جاري فتح الموقع مباشرة في المتصفح...
    start "" "%~dp0index.html"
)

pause
