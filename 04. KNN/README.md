![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white) ![Jupyter Notebook](https://img.shields.io/badge/Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)

# Bài 4: K láng giềng gần nhất (KNN)

**Họ và tên:** Đỗ Hoàng Phúc  
**MSSV:** 24748020101313  
**Môn:** Học Máy Và Ứng Dụng  
**LHP:** 261_71ITAI41203_0101  
**GVHD:** ThS. Nguyễn Thái Anh ([GitHub](https://github.com/AnhNguyenVLU))  

## 📌 Nội dung bài thực hành

Bài thực hành tìm hiểu và áp dụng thuật toán **K láng giềng gần nhất (K-Nearest Neighbors - KNN)** cho cả hai bài toán: phân loại (classification) và hồi quy (regression) trên 3 bộ dữ liệu: `data/sinh_vien_mo_rong.csv` (120 sinh viên), `data/hai_vang_trang.csv` (300 điểm có ranh giới cong) và `data/gia_nha.csv` (60 căn hộ).

Nội dung bao gồm:

* Tự tính khoảng cách Euclid và tìm láng giềng gần nhất bằng NumPy (áp dụng cơ chế vector hóa broadcasting)
* Tìm hiểu bản chất "học lười" (Lazy Learning) và nguyên lý hoạt động không tham số (non-parametric) của KNN
* Đo lường tác hại nghiêm trọng của việc quên chuẩn hóa đặc trưng khi có một cột mang thang đo lớn (`chi_tieu`)
* Đóng gói tiền xử lý chuẩn hóa và mô hình thành một khối thống nhất bằng `make_pipeline` (`StandardScaler` + `KNeighborsClassifier`) nhằm ngăn ngừa rò rỉ dữ liệu (data leakage)
* Khảo sát tác động của số lượng láng giềng $k$ (học vẹt khi $k=1$ và cẩu thả khi $k$ quá lớn)
* Lựa chọn siêu tham số $k$ tối ưu bằng kiểm định chéo 5 phần (`cross_val_score`) trên tập học mà không nhìn trộm tập kiểm tra
* So sánh KNN với Hồi quy Logistic và Naive Bayes trên dữ liệu có biên quyết định cong phi tuyến tính (bộ hai vầng trăng)
* Tìm hiểu lời nguyền số chiều (Curse of Dimensionality) khi số lượng đặc trưng tăng cao
* Ứng dụng KNN cho bài toán hồi quy (`KNeighborsRegressor`) trên dữ liệu giá nhà và phân tích giới hạn không ngoại suy được (extrapolation)
* Thực hiện các bài tập áp dụng từ 1 đến 6

## 📂 Nội dung mã nguồn
Hai notebook chính được sử dụng trong bài:

`code/Lab4_DoHoangPhuc.ipynb`

Notebook thực hiện các bước thực hành theo tài liệu Lab: tính khoảng cách và láng giềng bằng NumPy, khảo sát hậu quả khi quên chuẩn hóa, chọn $k$ bằng kiểm định chéo 5 phần, so sánh KNN với Hồi quy Logistic và Naive Bayes trên dữ liệu biên cong, ứng dụng KNN hồi quy và phân tích tính chất không ngoại suy.

`code/Baitaplab4.ipynb`

Notebook chứa lời giải cho 6 bài tập, bao gồm phần mã nguồn, kết quả tính toán và phần giải thích chi tiết.

## 📁 Cấu trúc thư mục

```text
04. KNN/
├── code/
│   ├── Baitaplab4.ipynb
│   └── Lab4_DoHoangPhuc.ipynb
├── data/
│   ├── gia_nha.csv
│   ├── hai_vang_trang.csv
│   └── sinh_vien_mo_rong.csv
├── figures/
├── outputs/
│   ├── Baitaplab4.txt
│   └── Lab4_DoHoangPhuc.txt
├── scripts/
│   └── run_all.py
├── README.md
└── requirements.txt
```
| Thư mục / tệp | Chức năng |
| --- | --- |
| `code/` | Chứa 2 notebook thực hành và bài tập. Chạy các cell theo thứ tự từ trên xuống để dữ liệu và biến được khởi tạo đầy đủ. |
| `code/Lab4_DoHoangPhuc.ipynb` | Các bước thực hành: tính khoảng cách, chuẩn hóa StandardScaler, chọn k tối ưu, so sánh mô hình và KNN hồi quy. |
| `code/Baitaplab4.ipynb` | Chứa lời giải bài tập 1–6, bao gồm mã nguồn, kết quả và phần giải thích chi tiết. |
| `data/gia_nha.csv` | Bộ dữ liệu 60 căn nhà dùng cho bài toán hồi quy. |
| `data/hai_vang_trang.csv` | Bộ dữ liệu 300 điểm phân bố theo hai vầng trăng khuyết có ranh giới cong phi tuyến tính. |
| `data/sinh_vien_mo_rong.csv` | Bộ dữ liệu 120 sinh viên với 3 đặc trưng `gio_on`, `diem_giua_ky`, `chi_tieu` và nhãn `qua_mon`. |
| `figures/` | Thư mục lưu các biểu đồ được tạo trong quá trình thực hành (nếu có). |
| `outputs/` | Lưu kết quả dạng văn bản sau khi chạy các notebook bằng `run_all.py`. |
| `scripts/run_all.py` | Script dùng để chạy toàn bộ notebook trong thư mục `code/` và lưu kết quả vào thư mục `outputs/`. |
| `requirements.txt` | Danh sách các thư viện Python cần thiết để chạy notebook và script. |
| `README.md` | Tài liệu hướng dẫn, giới thiệu nội dung bài thực hành, cấu trúc dự án và cách chạy chương trình. |

## 🛠️ Yêu cầu môi trường
Để chạy bài thực hành, cần cài đặt:  
Python 3.x  
Jupyter Notebook hoặc Visual Studio Code

Có thể kiểm tra phiên bản Python bằng:
```text
python --version
```
## 📦 Cài đặt thư viện
### Cách 1 – Sử dụng `requirements.txt`

Từ thư mục gốc của project, chạy:
```text
pip install -r requirements.txt
```

### Cách 2 – Cài đặt thủ công qua cmd
```text
pip install numpy pandas matplotlib scikit-learn notebook nbclient nbformat ipykernel
```

## ▶️ Cách chạy bài thực hành
### Cách 1 - Khởi động Jupyter Notebook:
```text
jupyter notebook
```
Sau đó mở:
`Lab4_DoHoangPhuc.ipynb`
hoặc:
`Baitaplab4.ipynb`
và chạy từng cell từ trên xuống dưới.

### Cách 2 - Chạy toàn bộ bằng script
Project có file:
`run_all.py`

Có thể chạy bằng:
```text
python scripts/run_all.py
```
Script dùng để thực hiện các chương trình được chuẩn bị sẵn trong project và lưu kết quả vào thư mục `outputs/`.

## ⚠️ Lưu ý
### 1. Chạy từ thư mục gốc
Nên chạy các lệnh từ thư mục: `04. KNN`
để đảm bảo các đường dẫn dữ liệu trong `data/` được nhận diện chính xác.

### 2. Không thay đổi cấu trúc thư mục
Các notebook sử dụng đường dẫn tương đối đến thư mục `data` và `outputs`.
Nếu thay đổi cấu trúc thư mục, chương trình có thể không tìm thấy file dữ liệu hoặc không lưu được kết quả.

### 3. Cài đặt thư viện trước khi chạy
Nếu xuất hiện lỗi:

`ModuleNotFoundError`

hãy chạy:
```text
pip install -r requirements.txt
```
