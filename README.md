![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white) ![Jupyter Notebook](https://img.shields.io/badge/Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)

# Machine Learning - Học Máy Và Ứng Dụng

**Họ và tên:** Đỗ Hoàng Phúc  
**MSSV:** 24748020101313  
**Môn:** Học Máy Và Ứng Dụng  
**LHP:** 261_71ITAI41203_0101  
**GVHD:** ThS. Nguyễn Thái Anh ([GitHub](https://github.com/AnhNguyenVLU))  

## 📌 Giới thiệu

Repository này tổng hợp các bài thực hành (**Lab**) của môn **Học Máy Và Ứng Dụng**.

Mỗi tuần học được tổ chức thành một thư mục riêng. Mỗi Lab có một file `README.md` riêng để trình bày:

* Nội dung bài thực hành
* Mục tiêu
* Cấu trúc thư mục
* Hướng dẫn cài đặt và chạy
* Mã nguồn
* Kết quả thực nghiệm
* Hình ảnh và nhận xét

## 📚 Danh sách bài thực hành

| Bài | Nội dung | Hướng dẫn |
| --- | --- | --- |
| 01 | **Hồi quy tuyến tính**: phân tích dữ liệu giá nhà, bình phương tối thiểu, đánh giá mô hình, gradient descent và hồi quy nhiều biến. | [01. Linear_Regression](https://github.com/dohoangphuc2006/Machine-Learning/blob/main/01.%20Linear_Regression/README.md) |
| 02 | **Hồi quy logistic**: phân tích dữ liệu sinh viên, hàm sigmoid, khớp mô hình phân loại, ma trận nhầm lẫn, ngưỡng quyết định và mô hình hai biến. | [02. Logistic_Regression](https://github.com/dohoangphuc2006/Machine-Learning/blob/main/02.%20Logistic_Regression/README.md) |
| 03 | **Naive Bayes**: định lý Bayes, tiền xử lý văn bản với CountVectorizer, bộ lọc tin nhắn rác MultinomialNB, hiện tượng số 0 và làm trơn Laplace, GaussianNB cho biến liên tục. | [03. Naive_Bayes](https://github.com/dohoangphuc2006/Machine-Learning/blob/main/03.%20Naive_Bayes/README.md) |
| 04 | **K láng giềng gần nhất (KNN)**: khoảng cách Euclid & Manhattan, chuẩn hóa StandardScaler & Pipeline, chọn k bằng kiểm định chéo, KNN phân loại và hồi quy. | [04. KNN](https://github.com/dohoangphuc2006/Machine-Learning/blob/main/04.%20KNN/README.md) |
| 05 | **Cây quyết định và Rừng ngẫu nhiên**: chỉ số Gini & Entropy, cắt tỉa cây max_depth & min_samples_leaf, kiểm chứng không cần chuẩn hóa, rừng ngẫu nhiên, độ quan trọng đặc trưng và hồi quy. | [05. DecisionTree_RandomForest](https://github.com/dohoangphuc2006/Machine-Learning/blob/main/05.%20DecisionTree_RandomForest/README.md) | 
| 06 | Lab 06 | Đang cập nhật | 

## 📂 Cấu trúc repository
```text
Machine-Learning/
├── 01. Linear_Regression/
│   ├── code/                 # Notebook thực hành và bài tập
│   ├── data/                 # Dữ liệu gia_nha.csv
│   ├── figures/              # Biểu đồ PNG
│   ├── outputs/              # Nhật ký kết quả
│   ├── scripts/              # run_all.py
│   ├── requirements.txt
│   └── README.md
├── 02. Logistic_Regression/
│   ├── code/                 # Notebook thực hành và bài tập
│   ├── data/                 # Dữ liệu sinh_vien.csv
│   ├── figures/              # Biểu đồ PNG
│   ├── outputs/              # Nhật ký kết quả
│   ├── scripts/              # run_all.py
│   ├── requirements.txt
│   └── README.md
├── 03. Naive_Bayes/
│   ├── code/                 # Notebook thực hành và bài tập
│   ├── data/                 # Dữ liệu sinh_vien.csv, tin_nhan.csv
│   ├── figures/              # Thư mục lưu biểu đồ
│   ├── outputs/              # Nhật ký kết quả
│   ├── scripts/              # run_all.py
│   ├── requirements.txt
│   └── README.md
├── 04. KNN/
│   ├── code/                 # Notebook thực hành và bài tập
│   ├── data/                 # Dữ liệu gia_nha.csv, hai_vang_trang.csv, sinh_vien_mo_rong.csv
│   ├── figures/              # Thư mục lưu biểu đồ
│   ├── outputs/              # Nhật ký kết quả
│   ├── scripts/              # run_all.py
│   ├── requirements.txt
│   └── README.md
├── 05. DecisionTree_RandomForest/
│   ├── code/                 # Notebook thực hành và bài tập
│   ├── data/                 # Dữ liệu gia_nha.csv, khach_vay.csv
│   ├── figures/              # Biểu đồ PNG
│   ├── outputs/              # Nhật ký kết quả
│   ├── scripts/              # run_all.py
│   ├── requirements.txt
│   └── README.md
├── .gitignore
└── README.md
```

## 🚀 Tải và chạy các bài thực hành

Clone repository hoặc chọn **Code → Download ZIP**, sau đó giải nén toàn bộ để giữ nguyên cấu trúc thư mục.

```sh
git clone https://github.com/dohoangphuc2006/Machine-Learning.git
cd Machine-Learning
```

## 📚 Chạy từng Lab
Mỗi Lab có README riêng chứa hướng dẫn cài đặt và chạy chi tiết:  
- [01. Linear_Regression](https://github.com/dohoangphuc2006/Machine-Learning/blob/main/01.%20Linear_Regression/README.md)   
- [02. Logistic_Regression](https://github.com/dohoangphuc2006/Machine-Learning/blob/main/02.%20Logistic_Regression/README.md)  
- [03. Naive_Bayes](https://github.com/dohoangphuc2006/Machine-Learning/blob/main/03.%20Naive_Bayes/README.md)  
- [04. KNN](https://github.com/dohoangphuc2006/Machine-Learning/blob/main/04.%20KNN/README.md)  
- [05. DecisionTree_RandomForest](https://github.com/dohoangphuc2006/Machine-Learning/blob/main/05.%20DecisionTree_RandomForest/README.md)  
