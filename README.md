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
| 06 | **Máy vectơ hỗ trợ (SVM)**: lề và vectơ hỗ trợ, tham số C, chuẩn hóa, kernel, dò lưới C–gamma và nhận dạng chữ số viết tay. | [06. SVM](https://github.com/dohoangphuc2006/Machine-Learning/blob/main/06.%20SVM/README.md) |
| 07 | **Đánh giá mô hình**: dữ liệu lệch lớp, mô hình lười, ma trận nhầm lẫn, precision–recall–F1, chọn ngưỡng, ROC–AUC và cân bằng lớp. | [07. Accuracy_Metrics](https://github.com/dohoangphuc2006/Machine-Learning/blob/main/07.%20Accuracy_Metrics/README.md) |
| 08 | **Phân cụm K-Means**: tự viết thuật toán, phân khúc khách hàng, chọn K bằng silhouette, khởi tạo tâm, nén màu ảnh và so sánh với DBSCAN. | [08. K-Means](https://github.com/dohoangphuc2006/Machine-Learning/blob/main/08.%20K-Means/README.md) |
| 09 | **Mạng nơ-ron nhiều lớp (MLP)**: lan truyền tiến, XOR, hàm kích hoạt, điều chuẩn, chuẩn hóa, tốc độ học, dò lưới và hồi quy. | [09. MLP](https://github.com/dohoangphuc2006/Machine-Learning/blob/main/09.%20MLP/README.md) |

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
├── 06. SVM/
│   ├── code/                 # Notebook thực hành và bài tập
│   ├── data/                 # sinh_vien.csv, sinh_vien_mo_rong.csv, hai_vang_trang.csv
│   ├── figures/              # Ảnh chữ số dự đoán sai
│   ├── outputs/              # Kết quả hai notebook dạng TXT
│   ├── scripts/              # run_all.py
│   ├── requirements.txt
│   └── README.md
├── 07. Accuracy_Metrics/
│   ├── code/                 # Notebook thực hành và bài tập
│   ├── data/                 # sinh_vien_bo_hoc.csv, gia_nha.csv
│   ├── figures/              # roc.png
│   ├── outputs/              # Kết quả hai notebook dạng TXT
│   ├── scripts/              # run_all.py
│   ├── requirements.txt
│   └── README.md
├── 08. K-Means/
│   ├── code/                 # Notebook thực hành và bài tập
│   ├── data/                 # khach_hang.csv, hai_vang_trang.csv, dohoangphuc3x4.jpg
│   ├── figures/              # Biểu đồ phân cụm và ảnh trước/sau nén màu
│   ├── outputs/              # Kết quả hai notebook dạng TXT
│   ├── scripts/              # run_all.py
│   ├── requirements.txt
│   └── README.md
├── 09. MLP/
│   ├── code/                 # Notebook thực hành và bài tập
│   ├── data/                 # xor.csv, hai_vang_trang.csv, sinh_vien_mo_rong.csv, gia_nha.csv
│   ├── figures/              # toc_do_hoc.png
│   ├── outputs/              # Kết quả hai notebook dạng TXT
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
- [06. SVM](https://github.com/dohoangphuc2006/Machine-Learning/blob/main/06.%20SVM/README.md)
- [07. Accuracy_Metrics](https://github.com/dohoangphuc2006/Machine-Learning/blob/main/07.%20Accuracy_Metrics/README.md)
- [08. K-Means](https://github.com/dohoangphuc2006/Machine-Learning/blob/main/08.%20K-Means/README.md)
- [09. MLP](https://github.com/dohoangphuc2006/Machine-Learning/blob/main/09.%20MLP/README.md)

### Chạy từng lab bằng script

Mỗi lab có `requirements.txt` và `scripts/run_all.py` riêng. Từ thư mục gốc repository, chuyển vào thư mục lab muốn chạy, cài thư viện rồi gọi script. Ví dụ với Lab 1:

```sh
cd "01. Linear_Regression"
python -m pip install -r requirements.txt
python scripts/run_all.py
```

Với lab khác, thay `01. Linear_Regression` bằng tên thư mục tương ứng trong danh sách trên. Hai lệnh cài thư viện và chạy script giữ nguyên khi terminal đã ở trong thư mục lab đó.

Các script chạy notebook trong `code/`, cập nhật kết quả notebook và lưu hai file TXT tương ứng vào `outputs/`. Những hình được mã nguồn lưu sẽ nằm trong `figures/`, kèm thông báo đường dẫn ngắn trong TXT. Lưu chỉnh sửa trong trình soạn thảo trước khi chạy vì script cập nhật notebook trên ổ đĩa.

Nếu mở notebook trực tiếp, chọn đúng kernel và chạy ô **Chuẩn bị** rồi các cell theo thứ tự. Các bài tập có nhận xét, giải thích cuối bài; các bước thực hành được chia theo tài liệu từng lab. Xem README của lab để biết các dataset, hình và kết quả cụ thể.

## ⚠️ Lưu ý khi chạy và đối chiếu kết quả

* Dùng môi trường Python có đủ thư viện, bao gồm `ipykernel`. Trong VS Code, kiểm tra **Python: Select Interpreter** và kernel notebook; việc một môi trường chạy được không có nghĩa môi trường khác đã cài đủ thư viện.
* Tham khảo README từng lab để chỉ định CSV ngoài `data/` hoặc chạy trên Google Colab. Giữ nguyên dữ liệu và cấu trúc thư mục khi tải repository về.
* Kết quả có thể thay đổi theo phiên bản Python, scikit-learn và thư viện số. Một số tham số ngẫu nhiên đã được cố định để hỗ trợ tái lập; thời gian huấn luyện còn phụ thuộc phần cứng.
* Lab 7 giữ cách dùng `SVC(probability=True)` của tài liệu và giới hạn scikit-learn dưới 1.11 trong requirements. Một số phiên bản vẫn in `FutureWarning`; đây là cảnh báo thay đổi API, không phải lỗi tính toán của lần chạy.
* Lab 8 so sánh dung lượng ảnh PNG thực tế với tỷ lệ biểu diễn bảng màu lý tưởng; hai con số không nhất thiết bằng nhau.
* Lab 9 có nhiều lần huấn luyện và dò lưới nên có thể chạy lâu.
* Dùng ảnh chụp màn hình khớp với lần chạy và các kết quả nộp. TXT và ảnh riêng lẻ không thay thế ảnh chụp màn hình nếu giảng viên yêu cầu.
