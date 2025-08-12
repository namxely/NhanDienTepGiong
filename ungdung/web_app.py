# -*- coding: utf-8 -*-
# YOLOv8 Shrimp Detection Web Application
# Fixed version for better detection and error handling

import sys
import os

# Fix Windows console encoding issues
if sys.platform == "win32":
    try:
        import locale
        locale.setlocale(locale.LC_ALL, 'C')
        # Also try to set console to UTF-8
        os.system("chcp 65001 > nul 2>&1")
    except:
        pass

print("NHAN DIEN TOM: Dang khoi dong ung dung...")

# Nhap cac thu vien can thiet voi xu ly loi
try:
    import cv2
    print("OK: OpenCV da nhap thanh cong (phien ban {})".format(cv2.__version__))
    
    import numpy as np
    print("OK: NumPy da nhap thanh cong (phien ban {})".format(np.__version__))
    
    from flask import Flask, render_template, request, jsonify
    print("OK: Flask da nhap thanh cong")
    
    from ultralytics import YOLO
    print("OK: Ultralytics YOLO da nhap thanh cong")
    
    import base64
    print("OK: Base64 da nhap thanh cong")
    
    from PIL import Image
    print("OK: PIL da nhap thanh cong")
    
    import io
    print("OK: IO da nhap thanh cong")
    
    print("THANH CONG: Tat ca thu vien da duoc nhap thanh cong!")
    
except ImportError as e:
    print("LOI: Khong the nhap cac thu vien can thiet: {}".format(e))
    print("Vui long cai dat cac goi can thiet bang lenh: pip install -r requirements.txt")
    input("Nhan Enter de thoat...")
    sys.exit(1)
except Exception as e:
    print("LOI: Loi khong mong muon khi nhap thu vien: {}".format(e))
    input("Nhan Enter de thoat...")
    sys.exit(1)

# Khoi tao ung dung Flask
app = Flask(__name__, template_folder='.')

# Bien toan cuc
model = None
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "..", "model", "best.pt")

def load_yolo_model():
    """Tai mo hinh YOLO voi xu ly loi"""
    global model
    print("MO HINH: Kiem tra mo hinh tai duong dan: {}".format(model_path))
    
    if os.path.exists(model_path):
        file_size = os.path.getsize(model_path)
        print("OK: Tim thay file mo hinh (kich thuoc: {} bytes)".format(file_size))
        try:
            print("DANG TAI: Dang tai mo hinh YOLO...")
            model = YOLO(model_path)
            print("THANH CONG: Mo hinh YOLO da duoc tai tu: {}".format(model_path))
            print("CAC LOP: Cac lop co san: {}".format(model.names))
            
            # Test model với một ảnh nhỏ để đảm bảo hoạt động
            test_img = np.zeros((416, 416, 3), dtype=np.uint8)
            test_results = model(test_img, conf=0.01, verbose=False)
            print("TEST: Mo hinh hoat dong binh thuong")
            
            return True
        except Exception as e:
            print("LOI: Khong the tai mo hinh YOLO: {}".format(e))
            import traceback
            traceback.print_exc()
            model = None
            return False
    else:
        print("LOI: Khong tim thay file mo hinh tai: {}".format(model_path))
        model = None
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mobile')
def mobile():
    """Giao dien responsive - chuyen ve trang chinh"""
    return render_template('index.html')

@app.route('/get_ip')
def get_ip():
    """Tra ve dia chi IP noi bo cho truy cap WiFi"""
    try:
        import socket
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return jsonify({"ip": local_ip})
    except Exception as e:
        return jsonify({"error": str(e), "ip": None})

@app.route('/test')
def test_page():
    """Trang kiem tra trang thai he thong"""
    import sys
    
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>TOM - Kiem tra he thong</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 20px; }
            .status { padding: 10px; margin: 10px 0; border-radius: 5px; }
            .success { background-color: #d4edda; color: #155724; }
            .error { background-color: #f8d7da; color: #721c24; }
            .info { background-color: #d1ecf1; color: #0c5460; }
        </style>
    </head>
    <body>
        <h1>TOM YOLOv8 - Kiem tra he thong nhan dien tom</h1>
    """
    
    html += '<div class="status info"><strong>Python:</strong> {}</div>'.format(sys.version)
    html += '<div class="status info"><strong>Thu muc lam viec:</strong> {}</div>'.format(os.getcwd())
    
    # Kiem tra cac thu vien
    try:
        import cv2
        html += '<div class="status success">OK OpenCV: {}</div>'.format(cv2.__version__)
    except:
        html += '<div class="status error">LOI OpenCV: Khong co san</div>'
    
    try:
        import numpy as np
        html += '<div class="status success">OK NumPy: {}</div>'.format(np.__version__)
    except:
        html += '<div class="status error">LOI NumPy: Khong co san</div>'
    
    try:
        from ultralytics import YOLO
        html += '<div class="status success">OK Ultralytics: Co san</div>'
    except:
        html += '<div class="status error">LOI Ultralytics: Khong co san</div>'
    
    # Kiem tra mo hinh
    if os.path.exists(model_path):
        html += '<div class="status success">OK File mo hinh: Tim thay ({} bytes)</div>'.format(os.path.getsize(model_path))
        if model is not None:
            html += '<div class="status success">OK Mo hinh da tai: {}</div>'.format(model.names)
        else:
            html += '<div class="status error">LOI Mo hinh chua duoc tai</div>'
    else:
        html += '<div class="status error">LOI File mo hinh: Khong tim thay tai {}</div>'.format(model_path)
    
    html += """
        <div class="status info">
            <h3>Dieu huong:</h3>
            <a href="/">TRANG CHU</a> | 
            <a href="/mobile">DIEN THOAI</a> | 
            <a href="/test">KIEM TRA</a>
        </div>
    </body>
    </html>
    """
    return html

def preprocess_image(frame):
    """Tiền xử lý ảnh để cải thiện khả năng nhận diện"""
    try:
        # Chuyển đổi về BGR nếu cần
        if len(frame.shape) == 3 and frame.shape[2] == 4:  # RGBA
            frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)
        elif len(frame.shape) == 3 and frame.shape[2] == 3:  # RGB
            # Kiểm tra xem có cần chuyển đổi RGB -> BGR không
            # Thử cả hai cách và giữ nguyên format tốt nhất
            pass
        
        # Cải thiện chất lượng ảnh
        # 1. Tăng độ tương phản
        lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        l = clahe.apply(l)
        enhanced = cv2.merge([l, a, b])
        enhanced = cv2.cvtColor(enhanced, cv2.COLOR_LAB2BGR)
        
        # 2. Giảm nhiễu nhẹ
        denoised = cv2.bilateralFilter(enhanced, 9, 75, 75)
        
        # 3. Tăng độ sắc nét
        kernel = np.array([[-1,-1,-1],
                          [-1, 9,-1],
                          [-1,-1,-1]])
        sharpened = cv2.filter2D(denoised, -1, kernel)
        
        # Trộn ảnh gốc và ảnh đã xử lý để tránh quá xử lý
        final = cv2.addWeighted(frame, 0.6, sharpened, 0.4, 0)
        
        return final
    except Exception as e:
        print("CANH BAO: Loi xu ly anh: {}. Su dung anh goc.".format(e))
        return frame

@app.route('/detect', methods=['POST'])
def detect():
    """Diem cuoi nhan dien chinh - da sua loi nang cao"""
    print("DETECT: Nhan duoc yeu cau nhan dien")
    
    if model is None:
        print("LOI: Mo hinh chua duoc tai")
        return jsonify({"error": "Mo hinh chua duoc tai"}), 500

    data = request.get_json()
    if not data or 'image' not in data:
        print("LOI: Khong nhan duoc du lieu hinh anh")
        return jsonify({"error": "Khong nhan duoc du lieu hinh anh"}), 400

    image_data_url = data['image']
    
    try:
        print("XU LY: Bat dau xu ly hinh anh...")
        # Trich xuat du lieu hinh anh tu data URL
        if "," in image_data_url:
            header, encoded = image_data_url.split(",", 1)
        else:
            encoded = image_data_url
            
        image_bytes = base64.b64decode(encoded)
        
        # Chuyen doi bytes thanh hinh anh OpenCV
        pil_image = Image.open(io.BytesIO(image_bytes))
        
        # Chuyển đổi sang RGB trước nếu cần
        if pil_image.mode != 'RGB':
            pil_image = pil_image.convert('RGB')
            
        frame = np.array(pil_image)
        
        # Chuyển đổi RGB -> BGR cho OpenCV
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            
        print("HINH ANH: Da xu ly hinh anh thanh cong: {}".format(frame.shape))
        
        # Tiền xử lý ảnh để cải thiện nhận diện
        processed_frame = preprocess_image(frame)
        print("XU LY: Da ap dung tien xu ly anh")

    except Exception as e:
        print("LOI: Giai ma hinh anh that bai: {}".format(e))
        import traceback
        traceback.print_exc()
        return jsonify({"error": "Giai ma hinh anh that bai: {}".format(str(e))}), 400

    try:
        # Chạy nhận diện với nhiều mức confidence khác nhau
        confidence_levels = [0.01, 0.05, 0.1, 0.25]
        best_results = None
        best_count = 0
        
        for conf_level in confidence_levels:
            print("NHAN DIEN: Thu voi confidence={}...".format(conf_level))
            
            # Thử với ảnh gốc
            results_orig = model(frame, conf=conf_level, iou=0.3, verbose=False)
            # Thử với ảnh đã xử lý
            results_processed = model(processed_frame, conf=conf_level, iou=0.3, verbose=False)
            
            # Chọn kết quả tốt hơn
            count_orig = 0
            count_processed = 0
            
            if results_orig and len(results_orig) > 0 and results_orig[0] is not None:
                if hasattr(results_orig[0], 'boxes') and results_orig[0].boxes is not None:
                    count_orig = len(results_orig[0].boxes)
                    
            if results_processed and len(results_processed) > 0 and results_processed[0] is not None:
                if hasattr(results_processed[0], 'boxes') and results_processed[0].boxes is not None:
                    count_processed = len(results_processed[0].boxes)
            
            # Chọn kết quả có nhiều detection hơn
            if count_processed > count_orig:
                current_results = results_processed
                current_count = count_processed
                print("   -> Su dung anh da xu ly: {} detections".format(count_processed))
            else:
                current_results = results_orig
                current_count = count_orig
                print("   -> Su dung anh goc: {} detections".format(count_orig))
            
            # Lưu kết quả tốt nhất
            if current_count > best_count:
                best_results = current_results
                best_count = current_count
                print("   -> Day la ket qua tot nhat hien tai!")
        
        print("--- THONG TIN DEBUG NHAN DIEN ---")
        print("DIEU VAO: Kich thuoc hinh anh: {}".format(frame.shape))
        print("CAC LOP: Cac lop mo hinh: {}".format(model.names))
        print("TOT NHAT: {} detections".format(best_count))
        
        detections = []
        shrimp_count = 0
        unique_species = set()

        if best_results and len(best_results) > 0 and best_results[0] is not None:
            result = best_results[0]
            print("OK: Mo hinh tra ve ket qua: {}".format(type(result)))
            
            # Kiem tra cac hop nhan dien
            if hasattr(result, 'boxes') and result.boxes is not None and len(result.boxes) > 0:
                num_boxes = len(result.boxes)
                print("HOP: Tim thay {} hop".format(num_boxes))
                
                # Trich xuat chi tiet nhan dien
                boxes_coords = result.boxes.xyxy.cpu().numpy()
                confidences = result.boxes.conf.cpu().numpy()
                class_ids = result.boxes.cls.cpu().numpy()
                
                print("DO TIN CAY: {}".format(confidences.tolist()))
                print("CAC LOP: ID cac lop: {}".format(class_ids.tolist()))
                
                # Tao ket qua nhan dien
                for i in range(num_boxes):
                    class_id = int(class_ids[i])
                    confidence = float(confidences[i])
                    
                    # Kiem tra xem class_id co hop le khong
                    if class_id in model.names:
                        species_name = model.names[class_id]
                    else:
                        species_name = f"Tom_Loai_{class_id}"
                        
                    box_coords = boxes_coords[i].tolist()
                    
                    # Đảm bảo tọa độ hợp lệ
                    box_coords = [max(0, coord) for coord in box_coords]
                    
                    print("   - Nhan dien {}: {} (do tin cay: {:.3f})".format(i+1, species_name, confidence))
                    
                    detections.append({
                        "box": box_coords,
                        "confidence": confidence,
                        "name": species_name
                    })
                    unique_species.add(species_name)
                
                shrimp_count = num_boxes
            else:
                print("THONG TIN: Khong tim thay hop nao")

            # Kiem tra mat na (phan doan) neu co
            if hasattr(result, 'masks') and result.masks is not None:
                num_masks = len(result.masks)
                print("MAT NA: Tim thay {} mat na".format(num_masks))
                if shrimp_count == 0:
                    shrimp_count = num_masks
            else:
                print("THONG TIN: Khong tim thay mat na")
                
        else:
            print("THONG TIN: Mo hinh khong tra ve ket qua nao!")
        
        print("TOM TAT: Tong cong {} tom duoc nhan dien".format(shrimp_count))
        print("LOAI: Cac loai: {}".format(list(unique_species)))
        print("--------------------------------")

        response_data = {
            "detections": detections, 
            "count": shrimp_count, 
            "species_detected": list(unique_species)
        }
        
        print("RESPONSE: Tra ve du lieu: {}".format(response_data))
        return jsonify(response_data)

    except Exception as e:
        print("LOI: Qua trinh nhan dien that bai: {}".format(e))
        import traceback
        traceback.print_exc()
        return jsonify({"error": "Qua trinh nhan dien that bai: {}".format(str(e))}), 500

if __name__ == '__main__':
    print("UNG DUNG NHAN DIEN TOM")
    print("Phat trien boi: Nguyen Thanh Nam - 0395212680")
    print("="*50)
    
    # Kiem tra cac phu thuoc truoc
    try:
        import torch
        print("OK: PyTorch {}".format(torch.__version__))
        if torch.cuda.is_available():
            print("OK: CUDA co san - GPU: {}".format(torch.cuda.get_device_name()))
        else:
            print("THONG TIN: Chi su dung CPU (khong co CUDA)")
    except ImportError:
        print("LOI: PyTorch chua duoc cai dat!")
    
    try:
        import ultralytics
        print("OK: Ultralytics {}".format(ultralytics.__version__))
    except ImportError:
        print("LOI: Ultralytics chua duoc cai dat!")
    
    print("MO HINH: Duong dan mo hinh: {}".format(model_path))
    print("FILE: Mo hinh ton tai: {}".format(os.path.exists(model_path)))
    
    # Tai mo hinh khi khoi dong
    model_loaded = load_yolo_model()
    
    if not model_loaded:
        print("CANH BAO: Khong the tai mo hinh! Ung dung se chay nhung nhan dien se khong hoat dong")
        print("LOI: Kiem tra file model/best.pt va cac phu thuoc")
        print("WEB: May chu kiem tra se chay tai: http://localhost:5000/test")
    else:
        print("THANH CONG: Mo hinh da duoc tai thanh cong!")
    
    # Lay dia chi IP noi bo
    try:
        import socket
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
    except:
        local_ip = "localhost"
    
    print("\nWEB: Ung dung dang chay tai:")
    print("   MAY TINH: http://localhost:5000")
    print("   WIFI/DIEN THOAI: http://{}:5000".format(local_ip))
    print("   GIAO DIEN THONG NHAT: Responsive cho moi thiet bi")
    print("   KIEM TRA: http://localhost:5000/test")
    print("\nDIEN THOAI: De su dung camera dien thoai:")
    print("   1. Ket noi dien thoai va may tinh vao cung WiFi")
    print("   2. Tren trinh duyet dien thoai, truy cap: http://{}:5000".format(local_ip))
    print("   3. Cho phep truy cap camera khi duoc hoi")
    print("\nCONFIDENCE: Ung dung se tu dong thu cac muc do tin cay de co ket qua tot nhat")
    print("DUNG: Nhan Ctrl+C de dung may chu\n")
    
    try:
        app.run(debug=False, host='0.0.0.0', port=5000)
    except Exception as e:
        print("LOI: Khong the khoi dong may chu: {}".format(e))
        import traceback
        traceback.print_exc()
        input("Nhan Enter de thoat...")
