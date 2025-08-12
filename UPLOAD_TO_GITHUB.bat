@echo off
chcp 65001 > nul
echo ========================================
echo     UPLOAD DU AN LEN GITHUB
echo ========================================
echo.

cd /d "%~dp0"

echo Kiem tra Git...
git --version >nul 2>&1
if errorlevel 1 (
    echo LOI: Git chua duoc cai dat!
    echo Vui long cai dat Git tu https://git-scm.com/
    pause
    exit /b 1
)

echo.
echo Khoi tao Git repository...
git init

echo.
echo Them tat ca file vao Git...
git add .

echo.
echo Commit lan dau...
git commit -m "Initial commit: YOLOv8 Shrimp Detection Application"

echo.
echo Them remote repository...
git remote add origin https://github.com/namxely/NhanDienTepGiong.git

echo.
echo Kiem tra remote...
git remote -v

echo.
echo Push len GitHub...
git branch -M main
git push -u origin main

echo.
echo HOAN THANH! Du an da duoc upload len GitHub.
echo Repository: https://github.com/namxely/NhanDienTepGiong.git
echo.
pause
