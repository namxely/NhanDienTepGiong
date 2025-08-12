# Chạy ứng dụng nhận diện tôm YOLOv8
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   HỆ THỐNG NHẬN DIỆN TÔM YOLOV8" -ForegroundColor Yellow
Write-Host "   Phiên bản đã sửa lỗi - Nâng cao" -ForegroundColor Yellow  
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Chuyển đến thư mục hiện tại
Set-Location $PSScriptRoot

Write-Host "Kiểm tra Python..." -ForegroundColor Green
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Lỗi: Python chưa được cài đặt!" -ForegroundColor Red
    Write-Host "Vui lòng cài đặt Python từ https://python.org" -ForegroundColor Yellow
    Read-Host "Nhấn Enter để thoát"
    exit 1
}

Write-Host "Kiểm tra các gói cần thiết..." -ForegroundColor Green
try {
    python -c "import cv2, numpy, flask, ultralytics, PIL" 2>$null
    if ($LASTEXITCODE -ne 0) {
        throw "Missing packages"
    }
    Write-Host "✓ Tất cả gói đã được cài đặt" -ForegroundColor Green
} catch {
    Write-Host "⚠ Đang cài đặt các gói cần thiết..." -ForegroundColor Yellow
    pip install -r requirements.txt
    if ($LASTEXITCODE -ne 0) {
        Write-Host "✗ Lỗi: Không thể cài đặt các gói cần thiết!" -ForegroundColor Red
        Read-Host "Nhấn Enter để thoát"
        exit 1
    }
}

Write-Host ""
Write-Host "🚀 Khởi động ứng dụng nhận diện tôm..." -ForegroundColor Cyan
Write-Host ""
Write-Host "HƯỚNG DẪN:" -ForegroundColor Yellow
Write-Host "1. Ứng dụng sẽ mở tại: http://localhost:5000" -ForegroundColor White
Write-Host "2. Sử dụng camera hoặc tải ảnh lên để nhận diện" -ForegroundColor White
Write-Host "3. Nhấn Ctrl+C để dừng" -ForegroundColor White
Write-Host ""

# Chuyển vào thư mục ungdung và chạy
Set-Location "ungdung"
try {
    python web_app.py
} finally {
    Write-Host ""
    Write-Host "Ứng dụng đã dừng." -ForegroundColor Yellow
    Read-Host "Nhấn Enter để thoát"
} 