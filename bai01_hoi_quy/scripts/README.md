![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white) ![Jupyter Notebook](https://img.shields.io/badge/Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)

# Bài 1:Hồi quy tuyến tính
👨‍🎓 Thông tin sinh viên
**Họ và tên:** Đỗ Hoàng Phúc  
**MSSV:** 24748020101313  
**Môn:** Học Máy Và Ứng Dụng  
**LHP:** 261_71ITAI41203_0101  
**GVHD:** ThS. Nguyễn Thái Anh ([GitHub](https://github.com/AnhNguyenVLU))  

## 📌 Nội dung bài thực hành

Bài thực hành tìm hiểu và áp dụng hồi quy tuyến tính (Linear Regression) trên bộ dữ liệu gồm 60 căn nhà trong file data/gia_nha.csv.

Nội dung bao gồm:

Đọc và kiểm tra dữ liệu bằng Pandas
Trực quan hóa dữ liệu bằng Matplotlib
Tính hệ số hồi quy tuyến tính
Tính sai số MSE
Xây dựng mô hình hồi quy tuyến tính bằng Scikit-learn
Chia dữ liệu thành tập huấn luyện và tập kiểm tra
Đánh giá mô hình bằng MAE, RMSE và R²
Tìm hiểu Gradient Descent
Xây dựng mô hình hồi quy tuyến tính với nhiều biến
Thực hiện các bài tập áp dụng từ 1 đến 6

## 📂 Nội dung mã nguồn
Hai notebook chính được sử dụng trong bài:

code/Lab1_DoHoangPhuc.ipynb

Notebook thực hiện các bước thực hành theo tài liệu Lab, bao gồm quá trình đọc dữ liệu, xây dựng mô hình, tính toán sai số, đánh giá mô hình và Gradient Descent.

code/Baitap.ipynb

Notebook chứa lời giải cho 6 bài tập, bao gồm phần xử lý dữ liệu, xây dựng mô hình, kết quả và nhận xét.

## 📁 Cấu trúc thư mục

```text
01. Linear_Regression/
├── code/
│   ├── Baitap.ipynb
│   └── Lab1_DoHoangPhuc.ipynb
├── data/
│   └── gia_nha.csv
├── figures/
│   ├── bai2.png
│   └── bai3.png
├── outputs/
│   ├── Lab1_DoHoangPhuc.txt
│   └── Baitap.txt
├── scripts/
│   └── run_all.py
├── README.md
└── requirements.txt
```
| Thư mục / tệp | Chức năng |
| --- | --- |
| [code/](code/) | Chứa 2 notebook thực hành và bài tập. Chạy các cell theo thứ tự từ trên xuống để dữ liệu và biến được khởi tạo đầy đủ. |
| [code/Lab1_DoHoangPhuc.ipynb](code/Lab1_DoHoangPhuc.ipynb) | Các bước thực hành: đọc dữ liệu, tính sai số, bình phương tối thiểu, sử dụng Scikit-learn, đánh giá mô hình, Gradient Descent và hồi quy nhiều biến. |
| [code/Baitap.ipynb](code/Baitap.ipynb) | Chứa lời giải bài tập 1–6, bao gồm mã nguồn, kết quả và phần nhận xét. |
| [data/gia_nha.csv](data/gia_nha.csv) | Bộ dữ liệu gồm 60 căn nhà với các thuộc tính `dien_tich`, `so_phong`, `tuoi_nha` và `gia`. Cần giữ tệp này để chạy chương trình. |
| [figures/](figures/) | Lưu các biểu đồ được tạo trong quá trình thực hành, bao gồm `bai2.png` và `bai3_tuoi_nha.png`. |
| [outputs/](outputs/) | Lưu kết quả dạng văn bản sau khi chạy các notebook bằng `run_all.py`. |
| [scripts/run_all.py](scripts/run_all.py) | Script dùng để chạy toàn bộ notebook trong thư mục `code/` và lưu kết quả vào thư mục `outputs/`. |
| [requirements.txt](requirements.txt) | Danh sách các thư viện Python cần thiết để chạy notebook và script. |
| [README.md](README.md) | Tài liệu hướng dẫn, giới thiệu nội dung bài thực hành, cấu trúc dự án và cách chạy chương trình. |

## 🛠️ Yêu cầu môi trường
Để chạy bài thực hành, cần cài đặt:
Python 3.x
Jupyter Notebook hoặc Visual Studio Code

Có thể kiểm tra phiên bản Python bằng:
```text
python --version
```
## 📦 Cài đặt thư viện
### Cách 1 – Sử dụng [requirements.txt](scripts/requirements.txt)

Từ thư mục gốc của project, chạy:
```text
pip install -r requirements.txt
```

### Cách 2 – Cài đặt thủ công
```text
pip install numpy pandas matplotlib scikit-learn notebook nbclient nbformat ipykernel
```

## ▶️ Cách chạy bài thực hành
### Cách 1 - Khởi động Jupyter Notebook:
jupyter notebook
Sau đó mở:
[Lab1_DoHoangPhuc.ipynb](code/Lab1_DoHoangPhuc.ipynb)
hoặc:

[Baitap.ipynb](code/Baitap.ipynb)
và chạy từng cell từ trên xuống dưới.

### Cách 2 - Chạy toàn bộ bằng script
Project có file:
[run_all.py](scripts/run_all.py)

Có thể chạy bằng:
```text
python scripts/run_all.py
```
Script dùng để thực hiện các chương trình được chuẩn bị sẵn trong project và lưu kết quả vào thư mục outputs/.

## ⚠️ Lưu ý
### 1. Chạy từ thư mục gốc
Nên chạy các lệnh từ thư mục: [bai01_hoi_quy](bai01_hoi_quy)
để đảm bảo đường dẫn: `data/gia_nha.csv` được nhận diện chính xác.

### 2. Không thay đổi cấu trúc thư mục
Các notebook sử dụng đường dẫn tương đối đến thư mục `data`, `figures` và `outputs`.
Nếu thay đổi cấu trúc thư mục, chương trình có thể không tìm thấy file dữ liệu hoặc không lưu được kết quả.

### 3. Cài đặt thư viện trước khi chạy
Nếu xuất hiện lỗi:

`ModuleNotFoundError`

hãy chạy:
```text
pip install -r requirements.txt
```
