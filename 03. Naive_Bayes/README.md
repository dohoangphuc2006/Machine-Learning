![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white) ![Jupyter Notebook](https://img.shields.io/badge/Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)

# Bài 3: Naive Bayes

**Họ và tên:** Đỗ Hoàng Phúc  
**MSSV:** 24748020101313  
**Môn:** Học Máy Và Ứng Dụng  
**LHP:** 261_71ITAI41203_0101  
**GVHD:** ThS. Nguyễn Thái Anh ([GitHub](https://github.com/AnhNguyenVLU))  

## 📌 Nội dung bài thực hành

Bài thực hành tìm hiểu và áp dụng thuật toán phân loại Naive Bayes trên dữ liệu văn bản (lọc tin nhắn rác trong file `data/tin_nhan.csv`) và dữ liệu số liên tục (dự đoán kết quả học tập trong file `data/sinh_vien.csv`).

Nội dung bao gồm:

* Đọc và khám phá kho tin nhắn bằng Pandas  
* Biến đổi dữ liệu văn bản thành bảng số bằng CountVectorizer (Bag of Words)  
* Tính định lý Bayes bằng tay (Prior, Likelihood, Posterior, Evidence)  
* Huấn luyện mô hình Multinomial Naive Bayes (MultinomialNB) bằng Scikit-learn  
* Đánh giá mô hình bằng Confusion Matrix, Accuracy, Precision và Recall  
* Tự cài đặt Naive Bayes từ đầu (không dùng thư viện) để thấy hiện tượng xác suất bằng 0 và kỹ thuật làm trơn Laplace (Laplace Smoothing)  
* Áp dụng Gaussian Naive Bayes (GaussianNB) cho đặc trưng liên tục và so sánh với Hồi quy Logistic  
* Thực hiện các bài tập áp dụng từ 1 đến 6  

## 📂 Nội dung mã nguồn
Hai notebook chính được sử dụng trong bài:

`code/Lab3_DoHoangPhuc.ipynb`

Notebook thực hiện các bước thực hành theo tài liệu Lab, bao gồm tính định lý Bayes bằng tay, tiền xử lý và số hóa văn bản bằng CountVectorizer, huấn luyện và đánh giá bộ lọc tin nhắn rác MultinomialNB, tự cài đặt Naive Bayes minh họa vấn đề xác suất bằng 0 và làm trơn Laplace, so sánh GaussianNB với Hồi quy Logistic trên dữ liệu liên tục.

`code/Baitaplab3.ipynb`

Notebook chứa lời giải cho 6 bài tập, bao gồm phần mã nguồn, kết quả tính toán và phần giải thích chi tiết

## 📁 Cấu trúc thư mục

```text
03. Naive_Bayes/
├── code/
│   ├── Baitaplab3.ipynb
│   └── Lab3_DoHoangPhuc.ipynb
├── data/
│   ├── sinh_vien.csv
│   └── tin_nhan.csv
├── figures/
├── outputs/
│   ├── Baitaplab3.txt
│   └── Lab3_DoHoangPhuc.txt
├── scripts/
│   └── run_all.py
├── README.md
└── requirements.txt
```
| Thư mục / tệp | Chức năng |
| --- | --- |
| `code/` | Chứa 2 notebook thực hành và bài tập. Chạy các cell theo thứ tự từ trên xuống để dữ liệu và biến được khởi tạo đầy đủ. |
| `code/Lab3_DoHoangPhuc.ipynb` | Các bước thực hành: định lý Bayes bằng tay, tiền xử lý CountVectorizer, mô hình MultinomialNB, tự cài đặt Naive Bayes và GaussianNB cho dữ liệu liên tục. |
| `code/Baitaplab3.ipynb` | Chứa lời giải bài tập 1–6, bao gồm mã nguồn, kết quả tính toán và phần nhận xét chi tiết. |
| `data/sinh_vien.csv` | Bộ dữ liệu sinh viên với các thuộc tính `gio_on`, `diem_giua_ky` và nhãn `qua_mon`. |
| `data/tin_nhan.csv` | Bộ dữ liệu gồm 300 tin nhắn với nội dung `noi_dung` và nhãn `la_rac` (1: rác, 0: thường). |
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
jupyter notebook
Sau đó mở:
`Lab3_DoHoangPhuc.ipynb`
hoặc:

`Baitaplab3.ipynb`
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
Nên chạy các lệnh từ thư mục: `03. Naive_Bayes`
để đảm bảo đường dẫn: `data/sinh_vien.csv` và `data/tin_nhan.csv` được nhận diện chính xác.

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
