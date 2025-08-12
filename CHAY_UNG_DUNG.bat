@echo off
chcp 65001 > nul
echo ========================================
echo    HE THONG NHAN DIEN TOM YOLOV8
echo    Phien ban da sua loi - Nang cao
echo ========================================
echo.

cd /d "%~dp0"

echo Kiem tra Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo LOI: Python chua duoc cai dat!
    echo Vui long cai dat Python tu https://python.org
    pause
    exit /b 1
)

echo Kiem tra cac goi can thiet...
python -c "import cv2, numpy, flask, ultralytics, PIL" >nul 2>&1
if errorlevel 1 (
    echo Dang cai dat cac goi can thiet...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo LOI: Khong the cai dat cac goi can thiet!
        pause
        exit /b 1
    )
)

echo Khoi dong ung dung nhan dien tom...
echo.
echo HUONG DAN:
echo 1. Ung dung se mo tai: http://localhost:5000
echo 2. Su dung camera hoac tai anh len de nhan dien
echo 3. Nhan Ctrl+C de dung
echo.

cd ungdung
python web_app.py

echo.
echo Ung dung da dung.
pause 