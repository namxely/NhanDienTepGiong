# 🦐 YOLOv8 Shrimp Detection Application

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-orange.svg)](https://ultralytics.com)
[![Flask](https://img.shields.io/badge/Flask-Web%20App-green.svg)](https://flask.palletsprojects.com)

Ứng dụng nhận diện và phân loại tôm cảnh sử dụng YOLOv8 với giao diện web hiện đại.

## 🌟 Tính năng

- **Nhận diện thời gian thực** qua camera web
- **Upload và phân tích ảnh** (đơn lẻ hoặc hàng loạt)
- **13 loại tôm** được hỗ trợ nhận diện
- **Giao diện web responsive** cho mọi thiết bị
- **Hỗ trợ điện thoại** qua WiFi
- **Confidence thông minh** tự động điều chỉnh
- **Tiền xử lý ảnh** để cải thiện độ chính xác

## 🎯 Các loài tôm được hỗ trợ

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

## 🚀 Cách sử dụng

### Cài đặt nhanh

```bash
# Clone repository
git clone https://github.com/namxely/NhanDienTepGiong.git
cd NhanDienTepGiong

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy ứng dụng
# Phương án 1: Double-click
CHAY_UNG_DUNG.bat

# Phương án 2: PowerShell
.\CHAY_UNG_DUNG.ps1

# Phương án 3: Manual
cd ungdung
python web_app.py
```

### Truy cập ứng dụng

- **Máy tính**: http://localhost:5000
- **Điện thoại**: http://[IP-máy-tính]:5000
- **Kiểm tra**: http://localhost:5000/test

## 📱 Sử dụng trên điện thoại

1. Kết nối cùng WiFi với máy tính
2. Tìm IP máy tính: `ipconfig` (Windows)
3. Truy cập: `http://[IP]:5000`
4. Cho phép quyền camera

## 🔧 Yêu cầu hệ thống

### Python Dependencies
```
opencv-python>=4.8.0
numpy>=1.24.0
flask>=2.3.0
ultralytics>=8.0.0
Pillow>=10.0.0
torch>=2.0.0
requests>=2.31.0
```

### Phần cứng
- **CPU**: Intel i5+ hoặc AMD Ryzen 5+
- **RAM**: 4GB+ (8GB khuyến nghị)
- **Storage**: 2GB+ dung lượng trống
- **Camera**: Tùy chọn cho nhận diện real-time

## 📊 Hiệu suất

- **Thời gian xử lý**: 1-3 giây/ảnh
- **Độ chính xác**: 85-95% (tùy chất lượng ảnh)
- **Confidence levels**: 0.01, 0.05, 0.1, 0.25 (tự động)
- **Supported formats**: JPG, JPEG, PNG

## 🛠️ Cấu trúc dự án

```
NhanDienTepGiong/
├── ungdung/
│   ├── web_app.py          # Backend Flask
│   └── index.html          # Frontend
├── model/
│   ├── best.pt             # Model YOLOv8 custom
│   ├── best.onnx           # Model ONNX
│   └── last.pt             # Checkpoint
├── CHAY_UNG_DUNG.bat       # Script Windows
├── CHAY_UNG_DUNG.ps1       # Script PowerShell
├── requirements.txt        # Dependencies
├── data.yaml              # Config dataset
└── README.md              # Hướng dẫn
```

## 🎯 Cách sử dụng

### 1. Camera real-time
1. Chọn camera từ dropdown
2. Nhấn "Bắt đầu"
3. Hướng camera về tôm
4. Xem kết quả nhận diện

### 2. Upload ảnh
1. Nhấn "Tải ảnh"
2. Chọn ảnh tôm
3. Chờ xử lý
4. Xem kết quả với bounding box

## ⚠️ Lưu ý

- **Sử dụng ảnh tôm thật** cho kết quả tốt nhất
- **Ánh sáng tốt** giúp cải thiện độ chính xác
- **Ảnh rõ nét** cho kết quả chính xác hơn
- **Model chỉ nhận diện 13 loài** đã được train

## 🐛 Troubleshooting

### Không nhận diện được?
- Kiểm tra ảnh có phải tôm thật
- Thử nhiều ảnh khác nhau
- Kiểm tra ánh sáng và độ rõ nét

### Lỗi camera?
- Refresh trang và thử lại
- Chọn camera khác
- Cho phép quyền camera

### Server không chạy?
- Kiểm tra Python version
- Cài đặt dependencies: `pip install -r requirements.txt`
- Kiểm tra port 5000 có bị chiếm

## 👨‍💻 Phát triển

**Author**: Nguyen Thanh Nam  
**Contact**: 0395212680  
**Framework**: YOLOv8 + Flask + OpenCV  
**Frontend**: HTML5 + TailwindCSS + JavaScript  

## 📝 License

MIT License - Xem file LICENSE để biết thêm chi tiết.

## 🙏 Acknowledgments

- [Ultralytics](https://ultralytics.com) cho YOLOv8
- [Flask](https://flask.palletsprojects.com) cho web framework
- [OpenCV](https://opencv.org) cho xử lý ảnh
- [TailwindCSS](https://tailwindcss.com) cho UI

---

⭐ **Star repository này nếu hữu ích!** ⭐
