# Upload dự án lên GitHub
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "     UPLOAD DỰ ÁN LÊN GITHUB" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Chuyển đến thư mục hiện tại
Set-Location $PSScriptRoot

Write-Host "Kiểm tra Git..." -ForegroundColor Green
try {
    $gitVersion = git --version 2>&1
    Write-Host "✓ $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Lỗi: Git chưa được cài đặt!" -ForegroundColor Red
    Write-Host "Vui lòng cài đặt Git từ https://git-scm.com/" -ForegroundColor Yellow
    Read-Host "Nhấn Enter để thoát"
    exit 1
}

Write-Host ""
Write-Host "Khởi tạo Git repository..." -ForegroundColor Yellow
try {
    git init
    Write-Host "✓ Git repository đã được khởi tạo" -ForegroundColor Green
} catch {
    Write-Host "⚠ Repository có thể đã tồn tại" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Thêm tất cả file vào Git..." -ForegroundColor Yellow
git add .
Write-Host "✓ Đã thêm tất cả file" -ForegroundColor Green

Write-Host ""
Write-Host "Commit lần đầu..." -ForegroundColor Yellow
try {
    git commit -m "Initial commit: YOLOv8 Shrimp Detection Application"
    Write-Host "✓ Commit thành công" -ForegroundColor Green
} catch {
    Write-Host "⚠ Có thể đã commit trước đó" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Thêm remote repository..." -ForegroundColor Yellow
try {
    git remote add origin https://github.com/namxely/NhanDienTepGiong.git
    Write-Host "✓ Remote repository đã được thêm" -ForegroundColor Green
} catch {
    Write-Host "⚠ Remote có thể đã tồn tại, cập nhật URL..." -ForegroundColor Yellow
    git remote set-url origin https://github.com/namxely/NhanDienTepGiong.git
}

Write-Host ""
Write-Host "Kiểm tra remote..." -ForegroundColor Yellow
git remote -v

Write-Host ""
Write-Host "🚀 Push lên GitHub..." -ForegroundColor Cyan
Write-Host "Bạn có thể cần nhập username/password hoặc token GitHub" -ForegroundColor Yellow
Write-Host ""

try {
    git branch -M main
    git push -u origin main
    
    Write-Host ""
    Write-Host "🎉 HOÀN THÀNH! Dự án đã được upload lên GitHub." -ForegroundColor Green
    Write-Host "Repository: https://github.com/namxely/NhanDienTepGiong.git" -ForegroundColor Cyan
    Write-Host ""
    
} catch {
    Write-Host ""
    Write-Host "❌ Có lỗi khi push lên GitHub:" -ForegroundColor Red
    Write-Host "Có thể bạn cần:" -ForegroundColor Yellow
    Write-Host "1. Đăng nhập GitHub: git config --global user.name 'YourName'" -ForegroundColor White
    Write-Host "2. Thiết lập email: git config --global user.email 'your@email.com'" -ForegroundColor White
    Write-Host "3. Tạo Personal Access Token trên GitHub" -ForegroundColor White
    Write-Host "4. Sử dụng token thay vì password khi push" -ForegroundColor White
    Write-Host ""
}

Write-Host "HƯỚNG DẪN THÊM:" -ForegroundColor Yellow
Write-Host "- Nếu repository private, cần token GitHub" -ForegroundColor White
Write-Host "- Nếu repository public, có thể push trực tiếp" -ForegroundColor White
Write-Host "- Xem README_GITHUB.md để biết thêm chi tiết" -ForegroundColor White

Read-Host "`nNhấn Enter để thoát"
