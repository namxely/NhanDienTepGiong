# 🦐 HƯỚNG DẪN SỬ DỤNG ỨNG DỤNG NHẬN DIỆN TÔM

## ✅ TÌNH TRẠNG ỨNG DỤNG

**ĐÃ KIỂM TRA - HOẠT ĐỘNG BÌNH THƯỜNG:**
- ✅ Server chạy ổn định tại `http://127.0.0.1:5000`
- ✅ Endpoint `/detect` hoạt động
- ✅ Model YOLO đã load thành công (13 loại tôm)
- ✅ Giao diện web responsive
- ✅ Backend xử lý ảnh không lỗi

## 🚀 CÁCH CHẠY ỨNG DỤNG

### Phương án 1: File Batch (Đơn giản)
```bash
# Double-click file này:
CHAY_UNG_DUNG.bat
```

### Phương án 2: PowerShell Script  
```powershell
# Click phải -> Run with PowerShell:
CHAY_UNG_DUNG.ps1
```

### Phương án 3: Manual
```bash
cd ungdung
python web_app.py
```

## 🌐 TRUY CẬP ỨNG DỤNG

- **Máy tính**: `http://localhost:5000`
- **Điện thoại cùng WiFi**: `http://[IP-máy-tính]:5000`
- **Trang kiểm tra**: `http://localhost:5000/test`

## 📸 CÁCH SỬ DỤNG

### 1. SỬ DỤNG CAMERA
1. Mở trình duyệt → `http://localhost:5000`
2. Chọn camera từ dropdown
3. Nhấn **"Bắt đầu"**
4. Hướng camera về phía tôm
5. Xem kết quả nhận diện real-time

### 2. UPLOAD ÁNH  
1. Nhấn **"Tải ảnh"**
2. Chọn một hoặc nhiều ảnh tôm
3. Chờ xử lý
4. Xem kết quả với bounding box

### 3. ẢNH TÔM PHẢI SỬ DỤNG

**✅ TỐT:**
- Ảnh tôm thật (từ chợ, ao nuôi, siêu thị)
- Ảnh có ánh sáng tốt
- Tôm rõ nét, không bị mờ
- Background không quá phức tạp

**❌ KHÔNG TỐT:**
- Ảnh fake, vẽ tay
- Ảnh quá mờ hoặc tối
- Ảnh có nhiều vật thể khác che khuất
- Hình vuông, hình tròn màu đỏ

## 🎯 MODEL NHẬN DIỆN

**13 LOẠI TÔM ĐƯỢC HỖ TRỢ:**
1. Tôm đốm đen
2. Tôm sét xanh  
3. Tôm pha lê đỏ đen
4. Tôm hổ họa tiết đen
5. Tôm vua khổng lồ đen
6. Tôm đồng cổ truyền
7. Tôm hổ mắt cam
8. Tôm gấu trúc đen
9. Tôm đốm đỏ
10. Tôm hổ gấu mèo
11. Tôm bóng mờ Mosura
12. Tôm hổ cam
13. Tôm vàng trắng

## 🔧 CONFIDENCE LEVELS

Ứng dụng tự động thử 4 mức độ tin cậy:
- **0.01** (rất thấp) - Bắt được nhiều tôm nhất
- **0.05** (thấp)
- **0.10** (trung bình)  
- **0.25** (cao)

## 📱 SỬ DỤNG TRÊN ĐIỆN THOẠI

1. **Kết nối cùng WiFi** với máy tính
2. **Tìm IP máy tính**:
   - Windows: `ipconfig`
   - Hoặc xem trong ứng dụng khi chạy
3. **Truy cập**: `http://[IP]:5000`
4. **Cho phép truy cập camera** khi được hỏi

## 🛠️ TROUBLESHOOTING

### Không nhận diện được tôm?
1. **Kiểm tra ảnh**: Phải là ảnh tôm thật
2. **Thử nhiều ảnh**: Model có thể không nhận diện tất cả
3. **Kiểm tra ánh sáng**: Ảnh quá tối sẽ khó nhận diện
4. **Test với ảnh mẫu**: Download ảnh tôm từ Google

### Lỗi camera?
1. **Refresh trang** và thử lại
2. **Chọn camera khác** từ dropdown
3. **Cho phép quyền camera** trên trình duyệt
4. **Thử trình duyệt khác** (Chrome, Edge, Firefox)

### Server không chạy?
1. **Kiểm tra Python**: `python --version`
2. **Cài đặt dependencies**: `pip install -r requirements.txt`
3. **Kiểm tra port 5000**: Có thể đang được sử dụng
4. **Chạy với admin** nếu cần

## 📊 HIỆU SUẤT

- **CPU**: Dùng CPU (không cần GPU)
- **RAM**: Khoảng 1-2GB  
- **Thời gian xử lý**: 1-3 giây/ảnh
- **Độ chính xác**: Phụ thuộc vào chất lượng ảnh

## 🎯 LỜI KHUYÊN

1. **Sử dụng ảnh tôm thật** cho kết quả tốt nhất
2. **Thử nhiều góc chụp** khác nhau  
3. **Ánh sáng tự nhiên** cho kết quả tốt hơn
4. **Upload nhiều ảnh cùng lúc** để tiết kiệm thời gian
5. **Sử dụng camera điện thoại** qua WiFi cho tiện lợi

## 📞 HỖ TRỢ

Nếu có vấn đề, kiểm tra:
1. Console log trong trình duyệt (F12)
2. Terminal chạy ứng dụng có báo lỗi gì
3. Trang `/test` để kiểm tra trạng thái hệ thống

---
**Phát triển bởi**: Nguyen Thanh Nam - 0395212680
**Cập nhật**: Đã sửa lỗi và tối ưu hóa nhận diện 