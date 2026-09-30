![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white) ![Jupyter Notebook](https://img.shields.io/badge/Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)

# Bài 2: Hồi quy Logistic

**Họ và tên:** Đỗ Hoàng Phúc  
**MSSV:** 24748020101313  
**Môn:** Học Máy Và Ứng Dụng  
**LHP:** 261_71ITAI41203_0101  
**GVHD:** ThS. Nguyễn Thái Anh ([GitHub](https://github.com/AnhNguyenVLU))  

## 📌 Nội dung bài thực hành

Bài thực hành tìm hiểu và áp dụng hồi quy logistic (Logistic Regression) để giải quyết bài toán phân loại nhị phân (dự đoán kết quả qua môn hoặc rớt môn) trên bộ dữ liệu gồm 120 sinh viên trong file `data/sinh_vien.csv`.

Nội dung bao gồm:

* Đọc và khám phá dữ liệu, so sánh đặc trưng giữa các lớp bằng Pandas
* Phân tích hạn chế của hồi quy tuyến tính trong bài toán phân loại nhị phân
* Tự cài đặt và kiểm chứng các tính chất của hàm Sigmoid bằng NumPy
* Xây dựng mô hình hồi quy logistic bằng Scikit-learn (`LogisticRegression`)
* Đọc hiểu hệ số hồi quy (\(w, b\)), tính mốc phân vân 50/50 và dự đoán xác suất (`predict_proba`)
* Chia dữ liệu có bảo toàn tỷ lệ nhãn (`stratify=y`) thành tập huấn luyện và tập kiểm tra
* Lập ma trận nhầm lẫn (Confusion Matrix) và tính toán bốn thước đo: Accuracy, Precision, Recall, \(F_1\)-score
* Khảo sát sự đánh đổi giữa Precision và Recall khi thay đổi ngưỡng quyết định (Decision Threshold)
* Mở rộng mô hình hồi quy logistic với hai biến đầu vào (`gio_on`, `diem_giua_ky`) và tìm hiểu biên quyết định (Decision Boundary)
* Thực hiện các bài tập áp dụng từ 1 đến 6

## 📂 Nội dung mã nguồn
Hai notebook chính được sử dụng trong bài:

`code/Lab2_DoHoangPhuc.ipynb`

Notebook thực hiện các bước thực hành theo tài liệu Lab, bao gồm quá trình đọc dữ liệu, xây dựng mô hình, tính toán sai số, đánh giá mô hình và Gradient Descent.

`code/Baitaplab2.ipynb`

Notebook chứa lời giải cho 6 bài tập, bao gồm phần xử lý dữ liệu, xây dựng mô hình, kết quả và nhận xét.

## 📁 Cấu trúc thư mục

```text
01. Linear_Regression/
├── code/
│   ├── Baitaplab2.ipynb
│   └── Lab2_DoHoangPhuc.ipynb
├── data/
│   └── sinh_vien.csv
├── figures/
│   ├── sigmoid.png
│   
├── outputs/
│   ├── Baitaplab2.txt
│   └── Lab2_DoHoangPhuc.txt
├── scripts/
│   └── run_all.py
├── README.md
└── requirements.txt
```
| Thư mục / tệp | Chức năng |
| --- | --- |
| `code/` | Chứa 2 notebook thực hành và bài tập. Chạy các cell theo thứ tự từ trên xuống để dữ liệu và biến được khởi tạo đầy đủ. |
| `code/Lab2_DoHoangPhuc.ipynb` | Các bước thực hành: đọc dữ liệu, tính sai số, bình phương tối thiểu, sử dụng Scikit-learn, đánh giá mô hình, Gradient Descent và hồi quy nhiều biến. |
| `code/Baitaplab2.ipynb` | Chứa lời giải bài tập 1–6, bao gồm mã nguồn, kết quả và phần nhận xét. |
| `data/sinh_vien.csv` | Bộ dữ liệu gồm 60 căn nhà với các thuộc tính `dien_tich`, `so_phong`, `tuoi_nha` và `gia`. Cần giữ tệp này để chạy chương trình. |
| `figures/` | Lưu các biểu đồ được tạo trong quá trình thực hành, bao gồm `bai2.png` và `bai3_tuoi_nha.png`. |
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
jupyter notebook
Sau đó mở:
`Lab1_DoHoangPhuc.ipynb`
hoặc:

`Baitap.ipynb`
và chạy từng cell từ trên xuống dưới.

### Cách 2 - Chạy toàn bộ bằng script
Project có file:
`run_all.py`

Có thể chạy bằng:
```text
python scripts/run_all.py
```
Script dùng để thực hiện các chương trình được chuẩn bị sẵn trong project và lưu kết quả vào thư mục outputs/.

## ⚠️ Lưu ý
### 1. Chạy từ thư mục gốc
Nên chạy các lệnh từ thư mục: `01. Linear_Regression`
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
