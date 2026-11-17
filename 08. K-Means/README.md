![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white) ![Jupyter Notebook](https://img.shields.io/badge/Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)

# Bài 8: Phân cụm K-Means

**Họ và tên:** Đỗ Hoàng Phúc  
**MSSV:** 24748020101313  
**Môn:** Học Máy Và Ứng Dụng  
**LHP:** 261_71ITAI41203_0101  
**GVHD:** ThS. Nguyễn Thái Anh ([GitHub](https://github.com/AnhNguyenVLU))  

## 📌 Nội dung bài thực hành

Bài thực hành tìm hiểu **K-Means** qua bài toán phân khúc khách hàng và nén màu ảnh. Các thí nghiệm khảo sát chuẩn hóa, lựa chọn số cụm, khởi tạo tâm và giới hạn của K-Means trên dữ liệu có hình dạng cong.

Nội dung bao gồm:

* Tự viết bước gán cụm và cập nhật tâm bằng NumPy trên bảy điểm
* Phân cụm 210 khách hàng theo thu nhập và điểm chi tiêu, đọc tâm theo đơn vị gốc
* Chọn số cụm bằng inertia và silhouette
* Khảo sát ba vấn đề: thang đo, khởi tạo tâm và cụm không có dạng tròn
* Nén màu ảnh mẫu bằng cách học trên một tập con điểm ảnh
* Thực hiện sáu bài tập: tự tính silhouette, thêm tuổi, so khởi tạo, lưu ảnh nén, DBSCAN và phân cụm chữ số

## 📂 Nội dung mã nguồn

Hai notebook chính được sử dụng trong bài:

`code/Lab8_DoHoangPhuc.ipynb`

Notebook gồm năm bước theo mã trong tài liệu Lab 8, mỗi bước có cell riêng. Ô chuẩn bị hỗ trợ tìm dữ liệu khi mở notebook từ các thư mục làm việc khác nhau.

`code/Baitaplab8.ipynb`

Notebook chứa sáu bài tập, kết quả và nhận xét, giải thích cuối mỗi bài bằng tiếng Việt có dấu. Nhãn kết quả tính toán dùng tiếng Việt không dấu. Bài 1 và bài 3 được giải thích kỹ theo tiêu chí chấm: định nghĩa silhouette, cách tính khoảng cách, cực tiểu cục bộ và vai trò của khởi tạo.

## 📁 Cấu trúc thư mục

```text
08. K-Means/
├── code/
│   ├── Baitaplab8.ipynb
│   └── Lab8_DoHoangPhuc.ipynb
├── data/
│   ├── dohoangphuc3x4.jpg
│   ├── hai_vang_trang.csv
│   └── khach_hang.csv
├── figures/
│   ├── anh_16_mau.png
│   ├── anh_goc.png
│   ├── bai1_silhouette.png
│   ├── bai5_dbscan.png
│   ├── dohoangphuc3x4_16_mau.png
│   └── dohoangphuc3x4_goc.png
├── outputs/
│   ├── Baitaplab8.txt
│   └── Lab8_DoHoangPhuc.txt
├── scripts/
│   └── run_all.py
├── README.md
└── requirements.txt
```

| Thư mục / tệp | Chức năng |
| --- | --- |
| `code/` | Hai notebook; chạy ô chuẩn bị rồi các cell theo thứ tự. |
| `code/Lab8_DoHoangPhuc.ipynb` | Năm bước thực hành theo tài liệu Lab 8. |
| `code/Baitaplab8.ipynb` | Lời giải bài tập 1–6 và phần giải thích cuối mỗi bài. |
| `data/khach_hang.csv` | 210 khách hàng, gồm `tuoi`, `thu_nhap`, `diem_chi_tieu`; không có nhãn cụm thật. |
| `data/hai_vang_trang.csv` | 300 điểm với `x1`, `x2`, `nhan`; nhãn thật chỉ dùng để đánh giá sau phân cụm. |
| `data/dohoangphuc3x4.jpg` | Ảnh cá nhân dùng cho phần nén ảnh của bài tập 4. |
| `figures/` | Biểu đồ silhouette, kết quả DBSCAN và ảnh trước/sau nén màu. |
| `outputs/` | Hai file TXT chứa kết quả và các thông báo lưu hình. |
| `scripts/run_all.py` | Chạy notebook thực hành rồi bài tập, cập nhật notebook và TXT. |
| `requirements.txt` | Thư viện cần thiết, gồm Pillow để đọc và ghi ảnh. |
| `README.md` | Giới thiệu nội dung, cấu trúc và cách chạy. |

## 🛠️ Yêu cầu môi trường

Để chạy bài thực hành, cần cài đặt:  
Python 3.11 trở lên  
Jupyter Notebook hoặc Visual Studio Code có hỗ trợ notebook

Kiểm tra phiên bản Python bằng:

```text
python --version
```

Các phiên bản thư viện chưa được cố định trong `requirements.txt`. Khác phiên bản có thể làm thay đổi một số kết quả khởi tạo, nhãn cụm, chữ số cuối và dung lượng ảnh. Số thứ tự cụm là tùy ý, không phải thứ hạng hay nhãn phân loại.

## 📦 Cài đặt thư viện

### Cách 1 – Sử dụng `requirements.txt`

Từ thư mục `08. K-Means`, chạy:

```text
python -m pip install -r requirements.txt
```

Nếu đang ở thư mục gốc repository, chạy:

```text
python -m pip install -r "08. K-Means/requirements.txt"
```

### Cách 2 – Cài đặt thủ công qua cmd

```text
python -m pip install numpy pandas matplotlib scikit-learn notebook nbclient nbformat ipykernel jupyter-client matplotlib-inline pillow
```

## ▶️ Cách chạy bài thực hành

### Cách 1 - Khởi động Jupyter Notebook:

Từ thư mục `08. K-Means`, chạy:

```text
jupyter notebook
```

Mở `code/Lab8_DoHoangPhuc.ipynb` hoặc `code/Baitaplab8.ipynb`, chạy ô **Chuẩn bị** trước rồi các cell từ trên xuống. Nếu dữ liệu nằm ở nơi khác, điền thư mục chứa dữ liệu vào `THU_MUC_DATA`. Trên Google Colab, tải các tệp được yêu cầu lên, gồm ảnh cá nhân ở bài tập 4.

Ảnh mẫu `china.jpg` và bộ chữ số `load_digits` có sẵn trong scikit-learn. Chạy notebook trực tiếp hiển thị kết quả và lưu hình; để cập nhật TXT, dùng script.

### Cách 2 - Chạy toàn bộ bằng script

Từ thư mục `08. K-Means`, chạy:

```text
python scripts/run_all.py
```

Hoặc từ thư mục gốc repository:

```text
python "08. K-Means/scripts/run_all.py"
```

Script dùng đúng Python đang gọi script, tạo kernel riêng cho từng notebook và lưu kết quả vào hai file TXT trong `outputs/`. Các ảnh được lưu vào `figures/`, kèm thông báo đường dẫn ngắn trong TXT.

Lưu các thay đổi trong trình soạn thảo trước khi chạy vì script cập nhật notebook trên ổ đĩa. Khi sửa mã hoặc dữ liệu, chạy lại để notebook, TXT và hình cùng phản ánh kết quả mới.

## ⚠️ Lưu ý

### 1. Chạy từ thư mục gốc của Lab 8

Dùng thư mục `08. K-Means` hoặc các lệnh dành cho thư mục gốc repository ở trên. Cách tìm dữ liệu hỗ trợ mở notebook từ thư mục gốc repository, thư mục lab và `code/`.

### 2. Không thay đổi cấu trúc thư mục

Giữ `data/`, `figures/` và `outputs/`. Nếu dữ liệu nằm nơi khác, chỉ định `THU_MUC_DATA` trong ô chuẩn bị hoặc truyền `--data-dir` cho script; thư mục thay thế cần chứa các tệp dùng trong notebook, gồm ảnh cá nhân. Đường dẫn có khoảng trắng phải đặt trong dấu nháy.

### 3. Cài đặt thư viện trước khi chạy

Nếu gặp `ModuleNotFoundError` hoặc thiếu `ipykernel_launcher`, cài thư viện vào đúng môi trường Python đang chạy script. Trong VS Code, chọn môi trường bằng **Python: Select Interpreter**, mở terminal mới và chọn kernel notebook tương ứng.

Silhouette cần ít nhất hai cụm; bài 1 tính trên dữ liệu đã chuẩn hóa. Bài 3 đếm inertia 23,0 sau khi làm tròn một chữ số theo mốc trong tài liệu. Bài 4 đo dung lượng PNG thực tế, phân biệt với tỷ lệ biểu diễn bảng màu lý tưởng. Bài 5 giữ nguyên các eps được yêu cầu và kết luận theo kết quả, không mặc định DBSCAN luôn tốt hơn K-Means.

