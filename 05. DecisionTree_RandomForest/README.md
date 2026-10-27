![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white) ![Jupyter Notebook](https://img.shields.io/badge/Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)

# Bài 5: Cây quyết định và Rừng ngẫu nhiên

**Họ và tên:** Đỗ Hoàng Phúc  
**MSSV:** 24748020101313  
**Môn:** Học Máy Và Ứng Dụng  
**LHP:** 261_71ITAI41203_0101  
**GVHD:** ThS. Nguyễn Thái Anh ([GitHub](https://github.com/AnhNguyenVLU))  

## 📌 Nội dung bài thực hành

Bài thực hành tìm hiểu và áp dụng thuật toán **Cây quyết định (Decision Tree)** và **Rừng ngẫu nhiên (Random Forest)** cho cả hai bài toán: phân loại khả năng trả nợ của khách hàng và hồi quy dự đoán giá nhà trên 2 bộ dữ liệu: `data/khach_vay.csv` (600 hồ sơ khách vay) và `data/gia_nha.csv` (60 căn hộ).

Nội dung bao gồm:

* Tự tính chỉ số hỗn tạp Gini và tìm câu hỏi phân chia tốt nhất bằng NumPy
* Học cây quyết định bằng Scikit-learn (`DecisionTreeClassifier`), đọc cấu trúc cây dạng văn bản (`export_text`) và trực quan hóa (`plot_tree`)
* Khảo sát hiện tượng cây học vẹt (quá khớp khi cây mọc tự do) và kỹ thuật cắt tỉa cây bằng `max_depth`, `min_samples_leaf`, `max_leaf_nodes`
* Lựa chọn độ sâu tối đa tối ưu bằng kiểm định chéo 5 phần (`cross_val_score`) trên tập học mà không nhìn trộm tập kiểm tra
* Kiểm chứng tính bất biến của cây quyết định đối với phép co giãn thang đo (cây không sợ đơn vị đo và không cần chuẩn hóa dữ liệu như KNN)
* Trồng rừng ngẫu nhiên (`RandomForestClassifier`) bằng cơ chế lấy mẫu có hoàn lại (Bootstrap) và chọn tập con đặc trưng ngẫu nhiên (Feature Bagging)
* Đọc và phân tích độ quan trọng của đặc trưng theo Gini (`feature_importances_`), nhận diện điểm hạn chế khi có cột ngẫu nhiên mang nhiều giá trị rời rạc
* Đánh giá độ quan trọng tin cậy hơn bằng kỹ thuật xáo trộn đặc trưng (`permutation_importance`)
* Ứng dụng cây và rừng cho bài toán hồi quy (`DecisionTreeRegressor`, `RandomForestRegressor`) trên dữ liệu giá nhà, phân tích bản chất dự đoán bậc thang và giới hạn không ngoại suy được
* Thực hiện các bài tập áp dụng từ 1 đến 6

## 📂 Nội dung mã nguồn
Hai notebook chính được sử dụng trong bài:

`code/Lab5_DoHoangPhuc.ipynb`

Notebook thực hiện các bước thực hành theo tài liệu Lab: tự tính chỉ số Gini trên 10 khách hàng, học cây 5 lá trên dữ liệu khách vay, chọn độ sâu qua kiểm định chéo, kiểm chứng cây không cần chuẩn hóa, trồng rừng ngẫu nhiên 200 cây, phân tích độ quan trọng của đặc trưng và cây hồi quy giá nhà.

`code/Baitaplab5.ipynb`

Notebook chứa lời giải cho 6 bài tập, bao gồm phần mã nguồn, kết quả tính toán và phần giải thích chi tiết.

## 📁 Cấu trúc thư mục

```text
05. DecisionTree_RandomForest/
├── code/
│   ├── Baitaplab5.ipynb
│   └── Lab5_DoHoangPhuc.ipynb
├── data/
│   ├── gia_nha.csv
│   └── khach_vay.csv
├── figures/
│   ├── cay_nam_la.png
│   └── cay_sau_2.png
├── outputs/
│   ├── Baitaplab5.txt
│   └── Lab5_DoHoangPhuc.txt
├── scripts/
│   └── run_all.py
├── README.md
└── requirements.txt
```
| Thư mục / tệp | Chức năng |
| --- | --- |
| `code/` | Chứa 2 notebook thực hành và bài tập. Chạy các cell theo thứ tự từ trên xuống để dữ liệu và biến được khởi tạo đầy đủ. |
| `code/Lab5_DoHoangPhuc.ipynb` | Các bước thực hành: tính Gini, học cây 5 lá, chọn độ sâu qua kiểm định chéo, kiểm chứng không chuẩn hóa, trồng rừng ngẫu nhiên, độ quan trọng đặc trưng và cây hồi quy. |
| `code/Baitaplab5.ipynb` | Chứa lời giải bài tập 1–6, bao gồm mã nguồn, kết quả và phần giải thích chi tiết. |
| `data/gia_nha.csv` | Bộ dữ liệu 60 căn nhà dùng cho bài toán hồi quy. |
| `data/khach_vay.csv` | Bộ dữ liệu 600 khách vay với các thuộc tính `thu_nhap`, `ty_le_no`, `co_viec_on_dinh`, `so_nguoi_phu_thuoc` và nhãn `tra_dung_han`. |
| `figures/` | Thư mục lưu các biểu đồ được tạo trong quá trình thực hành (`cay_nam_la.png`, `cay_sau_2.png`). |
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
`Lab5_DoHoangPhuc.ipynb`
hoặc:
`Baitaplab5.ipynb`
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
Nên chạy các lệnh từ thư mục: `05. DecisionTree_RandomForest`
để đảm bảo các đường dẫn dữ liệu trong `data/` được nhận diện chính xác.

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
