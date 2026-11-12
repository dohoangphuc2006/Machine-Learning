![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white) ![Jupyter Notebook](https://img.shields.io/badge/Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)

# Bài 6: Máy vectơ hỗ trợ (SVM)

**Họ và tên:** Đỗ Hoàng Phúc  
**MSSV:** 24748020101313  
**Môn:** Học Máy Và Ứng Dụng  
**LHP:** 261_71ITAI41203_0101  
**GVHD:** ThS. Nguyễn Thái Anh ([GitHub](https://github.com/AnhNguyenVLU))  

## 📌 Nội dung bài thực hành

Bài thực hành tìm hiểu và áp dụng **Máy vectơ hỗ trợ (SVM)** cho bài toán phân loại trên các bộ dữ liệu sinh viên, hai vầng trăng và chữ số viết tay. Ba tệp CSV nằm trong `data/`; dữ liệu chữ số được nạp từ scikit-learn.

Nội dung bao gồm:

* Tìm đường phân chia có lề rộng nhất và xác định các vectơ hỗ trợ
* Khảo sát tác động của tham số `C` và việc chuẩn hóa đặc trưng
* So sánh kernel tuyến tính, đa thức và RBF trên dữ liệu hai vầng trăng
* Chọn `C` và `gamma` bằng kiểm định chéo với `GridSearchCV`
* Phân loại chữ số viết tay bằng SVM và phân tích các ảnh dự đoán sai
* Thực hiện sáu bài tập, gồm tính hàm quyết định, quan sát thay đổi ranh giới, lựa chọn mô hình và so sánh thời gian huấn luyện

## 📂 Nội dung mã nguồn

Hai notebook chính được sử dụng trong bài:

`code/Lab6_DoHoangPhuc.ipynb`

Notebook thực hiện năm bước thực hành theo tài liệu Lab 6: lề rộng nhất, tham số `C` và chuẩn hóa, các loại kernel, dò lưới tham số, nhận dạng chữ số viết tay. Các bước được chia thành các cell mã riêng. Ô chuẩn bị hỗ trợ tìm các tệp CSV khi mở notebook ở những thư mục làm việc khác nhau.

`code/Baitaplab6.ipynb`

Notebook chứa lời giải sáu bài tập, kết quả tính toán và phần nhận xét, giải thích bằng tiếng Việt ở cuối mỗi bài. Bài 1 và bài 2 giải thích kỹ hàm quyết định, lề và vectơ hỗ trợ theo tiêu chí chấm.

## 📁 Cấu trúc thư mục

```text
06. SVM/
├── code/
│   ├── Baitaplab6.ipynb
│   └── Lab6_DoHoangPhuc.ipynb
├── data/
│   ├── hai_vang_trang.csv
│   ├── sinh_vien.csv
│   └── sinh_vien_mo_rong.csv
├── figures/
│   ├── bai5_anh_006_that_9_doan_3.png
│   ├── bai5_anh_018_that_8_doan_1.png
│   ├── bai5_anh_161_that_4_doan_8.png
│   └── bai5_anh_428_that_7_doan_9.png
├── outputs/
│   ├── Baitaplab6.txt
│   └── Lab6_DoHoangPhuc.txt
├── scripts/
│   └── run_all.py
├── README.md
└── requirements.txt
```

| Thư mục / tệp | Chức năng |
| --- | --- |
| `code/` | Chứa hai notebook thực hành và bài tập. Chạy ô chuẩn bị trước, sau đó chạy các cell theo thứ tự. |
| `code/Lab6_DoHoangPhuc.ipynb` | Năm bước thực hành SVM theo tài liệu Lab 6. |
| `code/Baitaplab6.ipynb` | Lời giải bài tập 1–6 với kết quả và phần giải thích cuối mỗi bài. |
| `data/sinh_vien.csv` | Dữ liệu sinh viên với đặc trưng `gio_on`, `diem_giua_ky` và nhãn `qua_mon`. |
| `data/sinh_vien_mo_rong.csv` | Dữ liệu sinh viên có thêm đặc trưng `chi_tieu` để khảo sát ảnh hưởng của thang đo. |
| `data/hai_vang_trang.csv` | Dữ liệu hai vầng trăng với đặc trưng `x1`, `x2` và nhãn `nhan`. |
| `figures/` | Lưu ảnh chữ số được dự đoán sai trong bài tập 5. |
| `outputs/` | Lưu kết quả dạng văn bản của hai notebook sau khi chạy `run_all.py`. |
| `scripts/run_all.py` | Chạy lần lượt hai notebook và lưu kết quả vào `outputs/`. |
| `requirements.txt` | Danh sách thư viện Python cần thiết. |
| `README.md` | Giới thiệu nội dung, cấu trúc và cách chạy bài thực hành. |

## 🛠️ Yêu cầu môi trường

Để chạy bài thực hành, cần cài đặt:  
Python 3.11 trở lên  
Jupyter Notebook hoặc Visual Studio Code có hỗ trợ notebook

Có thể kiểm tra phiên bản Python bằng:

```text
python --version
```

Kết quả số ở chữ số cuối có thể thay đổi theo phiên bản thư viện; thời gian huấn luyện ở bài tập 6 còn phụ thuộc máy chạy. Các phiên bản thư viện trong `requirements.txt` chưa được cố định.

## 📦 Cài đặt thư viện

### Cách 1 – Sử dụng `requirements.txt`

Từ thư mục `06. SVM`, chạy:

```text
python -m pip install -r requirements.txt
```

Nếu đang ở thư mục gốc repository, chạy:

```text
python -m pip install -r "06. SVM/requirements.txt"
```

### Cách 2 – Cài đặt thủ công qua cmd

```text
python -m pip install numpy pandas matplotlib scikit-learn notebook nbclient nbformat ipykernel
```

## ▶️ Cách chạy bài thực hành

### Cách 1 - Khởi động Jupyter Notebook:

Từ thư mục `06. SVM`, chạy:

```text
jupyter notebook
```

Sau đó mở `code/Lab6_DoHoangPhuc.ipynb` hoặc `code/Baitaplab6.ipynb`, chạy ô **Chuẩn bị** rồi chạy từng cell từ trên xuống. Nếu CSV nằm ngoài `data/`, gán đường dẫn vào các biến `DUONG_DAN_SINH_VIEN`, `DUONG_DAN_SINH_VIEN_MO_RONG`, `DUONG_DAN_VANG_TRANG` ở ô chuẩn bị. Trên Google Colab, tải ba CSV lên khi notebook yêu cầu.

### Cách 2 - Chạy toàn bộ bằng script

Từ thư mục `06. SVM`, chạy:

```text
python scripts/run_all.py
```

Hoặc từ thư mục gốc repository:

```text
python "06. SVM/scripts/run_all.py"
```

Script thực thi notebook thực hành rồi notebook bài tập, lưu kết quả TXT trong `outputs/`; bài tập 5 lưu ảnh dự đoán sai trong `figures/`. Sau khi sửa mã hoặc dữ liệu, chạy lại script để kết quả notebook, TXT và ảnh phản ánh cùng một lần chạy. Nên lưu các thay đổi trong trình soạn thảo trước khi chạy script vì script cập nhật notebook trên ổ đĩa.

## ⚠️ Lưu ý

### 1. Chạy từ thư mục gốc của Lab 6

Nên chạy các lệnh từ thư mục `06. SVM` để các đường dẫn tương đối được nhận diện đúng. Script cũng có thể được gọi từ thư mục gốc repository như lệnh ở trên.

### 2. Không thay đổi cấu trúc thư mục

Notebook và script dùng các thư mục `data/`, `figures/` và `outputs/`. Nếu dữ liệu nằm nơi khác, có thể chỉ định đường dẫn ở ô chuẩn bị hoặc dùng các tùy chọn `--sinh-vien`, `--sinh-vien-mo-rong`, `--vang-trang` của script.

### 3. Cài đặt thư viện trước khi chạy

Nếu gặp `ModuleNotFoundError`, cài thư viện từ `requirements.txt` và kiểm tra notebook đang dùng đúng môi trường Python đã cài.
