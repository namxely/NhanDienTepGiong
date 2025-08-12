# Ứng Dụng Nhận Diện Tôm YOLOv8

**Nhà phát triển:** Nguyễn Thành Nam  
**Điện thoại:** 0395212680  
**Email:** [namnguyen2452003@gmail.com]

## Tổng Quan

Ứng dụng nhận diện tôm chuyên nghiệp sử dụng YOLOv8 với giao diện web Flask, hỗ trợ camera máy tính và điện thoại di động.

## Cách Sử Dụng Nhanh

### Phương pháp 1: Khởi động đơn giản (Khuyến nghị)
```bash
# Nhấp đúp vào file batch để khởi động dễ dàng
KHOI_DONG_UNG_DUNG.bat
```

### Phương pháp 2: Cài đặt thủ công
```bash
# 1. Cài đặt các thư viện cần thiết
pip install -r requirements.txt

# 2. Khởi động ứng dụng
python ungdung/web_app.py
```

## Các Script Có Sẵn

| Script | Mô tả |
|--------|-------|
| `KHOI_DONG_UNG_DUNG.bat` | Khởi động ứng dụng đơn giản (Tiếng Việt) |

## Đường Dẫn Truy Cập

- **Máy tính:** http://localhost:5000
- **Điện thoại:** http://localhost:5000/mobile  
- **Kiểm tra hệ thống:** http://localhost:5000/test

## Cài Đặt Camera Điện Thoại

1. Kết nối điện thoại và máy tính vào cùng mạng WiFi
2. Mở trình duyệt trên điện thoại
3. Truy cập: `http://[địa-chỉ-ip-máy-tính]:5000/mobile`
4. Cho phép truy cập camera khi được yêu cầu

## Cấu Trúc Ứng Dụng

```
ungdung/
├── web_app.py              # Ứng dụng Flask chính
├── index.html              # Giao diện web máy tính
├── mobile_camera.html      # Giao diện tối ưu cho di động
├── guide.html              # Hướng dẫn cài đặt
├── huong_dan_camera.html   # Hướng dẫn cài đặt camera (Tiếng Việt)
└── camera_config.js        # Cấu hình camera

model/
├── best.pt                 # Mô hình YOLOv8 đã huấn luyện
├── best.onnx              # Mô hình định dạng ONNX
└── last.pt                # Checkpoint mới nhất
```

## Tính Năng

- **Nhận diện thời gian thực:** Xử lý luồng camera trực tiếp
- **Tải ảnh lên:** Phân tích ảnh tĩnh  
- **Hỗ trợ di động:** Tích hợp camera điện thoại
- **Truy cập đa thiết bị:** Giao diện máy tính và di động
- **Hiển thị độ tin cậy:** Điểm số độ tin cậy của việc nhận diện
- **Tương thích Windows:** Không có vấn đề Unicode/emoji

## Cấu Hình

### Cài Đặt Mô Hình
- **Ngưỡng độ tin cậy:** 0.1 (có thể điều chỉnh trong web_app.py)
- **Ngưỡng IOU:** 0.5
- **Định dạng mô hình:** PyTorch (.pt)

### Cài Đặt Camera
- **Độ phân giải:** Tự động phát hiện
- **Tốc độ khung hình:** 30 FPS (giao diện web)
- **Định dạng hỗ trợ:** JPEG, PNG

## Điểm Cuối API

### GET /
Giao diện ứng dụng chính

### GET /mobile
Giao diện tối ưu cho di động

### GET /test
Trạng thái hệ thống và chẩn đoán

### POST /detect
Điểm cuối API nhận diện
```json
{
  "image": "data:image/jpeg;base64,..."
}
```

Phản hồi:
```json
{
  "detections": [...],
  "count": 5,
  "species_detected": ["loài1", "loài2"]
}
```

## Khắc Phục Sự Cố

### Ứng dụng không khởi động được
1. Kiểm tra cài đặt Python: `python --version`
2. Cài đặt thư viện cần thiết: `pip install -r requirements.txt`
3. Xác minh file mô hình tồn tại: `model/best.pt`
4. Kiểm tra vấn đề mã hóa console Windows

### Không tìm thấy nhận diện
1. Kiểm tra việc tải mô hình tại trang `/test`
2. Xác minh ngưỡng độ tin cậy (thử giảm xuống 0.05)
3. Kiểm tra chất lượng ảnh và ánh sáng
4. Đảm bảo mô hình được tải đúng cách

### Vấn đề truy cập camera
1. Cho phép quyền truy cập camera trình duyệt
2. Kiểm tra driver camera
3. Thử các trình duyệt khác
4. Khởi động lại ứng dụng

### Vấn đề kết nối di động
1. Xác minh kết nối WiFi (cùng mạng)
2. Kiểm tra cài đặt tường lửa
3. Sử dụng đúng địa chỉ IP
4. Thử trình duyệt di động khác

## Thư Viện Cần Thiết

- **Python 3.8+**
- **OpenCV:** Xử lý hình ảnh
- **Flask:** Framework web
- **Ultralytics:** Triển khai YOLOv8
- **NumPy:** Tính toán số học
- **Pillow:** Xử lý hình ảnh
- **PyTorch:** Backend deep learning

## Cập Nhật & Bảo Trì

### Cập Nhật Mô Hình
1. Thay thế `model/best.pt` bằng mô hình mới
2. Khởi động lại ứng dụng
3. Kiểm tra độ chính xác nhận diện

### Cập Nhật Thư Viện
```bash
pip install --upgrade -r requirements.txt
```

## Hiệu Suất

- **Tốc độ nhận diện:** ~100ms mỗi khung hình
- **Sử dụng bộ nhớ:** ~2GB (với mô hình đã tải)
- **Độ phân giải hỗ trợ:** Lên đến 4K
- **Người dùng đồng thời:** 10+ (tùy thuộc phần cứng)

## Lưu Ý Bảo Mật

- Ứng dụng chỉ chạy trên mạng nội bộ
- Không lưu trữ dữ liệu vĩnh viễn
- Hình ảnh chỉ được xử lý trong bộ nhớ
- HTTPS chưa được cấu hình (sử dụng nội bộ)

## Hỗ Trợ

Để được hỗ trợ kỹ thuật hoặc có câu hỏi:
- **Nhà phát triển:** Nguyễn Thành Nam
- **Điện thoại:** 0395212680
- **Vấn đề:** Vui lòng kiểm tra phần khắc phục sự cố trước


**Cập nhật lần cuối:** Tháng 6 năm 2025  

