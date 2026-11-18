![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white) ![Jupyter Notebook](https://img.shields.io/badge/Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)

# Bài 9: Mạng nơ-ron nhiều lớp (MLP)

**Họ và tên:** Đỗ Hoàng Phúc  
**MSSV:** 24748020101313  
**Môn:** Học Máy Và Ứng Dụng  
**LHP:** 261_71ITAI41203_0101  
**GVHD:** ThS. Nguyễn Thái Anh ([GitHub](https://github.com/AnhNguyenVLU))  

## 📌 Nội dung bài thực hành

Bài thực hành tìm hiểu **mạng nơ-ron nhiều lớp (MLP)** từ phép tính lan truyền tiến đến huấn luyện mô hình phân loại và hồi quy bằng scikit-learn. Dữ liệu gồm XOR, hai vầng trăng, sinh viên mở rộng, giá nhà và bộ chữ số viết tay.

Nội dung bao gồm:

* Tự tính một nơ-ron sigmoid và mạng giải XOR bằng NumPy
* So sánh hồi quy logistic với mạng có một lớp ẩn trên XOR
* Khảo sát độ lớn mạng, hiện tượng học vẹt và điều chuẩn L2 bằng `alpha`
* Kiểm tra ảnh hưởng của chuẩn hóa và chọn tham số bằng kiểm định chéo
* Nhận dạng chữ số, đọc trọng số, đếm tham số và khảo sát dừng sớm
* Thực hiện sáu bài tập về lan truyền tiến, ReLU, hàm kích hoạt, tốc độ học, dò lưới và hồi quy giá nhà

## 📂 Nội dung mã nguồn

Hai notebook chính được sử dụng trong bài:

`code/Lab9_DoHoangPhuc.ipynb`

Notebook gồm năm bước thực hành theo mã trong tài liệu Lab 9, mỗi bước có cell riêng. Ô chuẩn bị hỗ trợ tìm dữ liệu từ nhiều thư mục làm việc và hiển thị cảnh báo thư viện mà không kèm đường dẫn cài đặt cá nhân.

`code/Baitaplab9.ipynb`

Notebook chứa sáu bài tập với kết quả và nhận xét, giải thích cuối mỗi bài bằng tiếng Việt có dấu. Nhãn kết quả tính toán dùng tiếng Việt không dấu. Bài 1 và bài 2 được giải thích kỹ theo tiêu chí chấm: phép nhân ma trận, hệ số chặn, ReLU, sigmoid và cách mạng tính XOR.

## 📁 Cấu trúc thư mục

```text
09. MLP/
├── code/
│   ├── Baitaplab9.ipynb
│   └── Lab9_DoHoangPhuc.ipynb
├── data/
│   ├── gia_nha.csv
│   ├── hai_vang_trang.csv
│   ├── sinh_vien_mo_rong.csv
│   └── xor.csv
├── figures/
│   └── toc_do_hoc.png
├── outputs/
│   ├── Baitaplab9.txt
│   └── Lab9_DoHoangPhuc.txt
├── scripts/
│   └── run_all.py
├── README.md
└── requirements.txt
```

| Thư mục / tệp | Chức năng |
| --- | --- |
| `code/` | Hai notebook; chạy ô chuẩn bị rồi các cell theo thứ tự. |
| `code/Lab9_DoHoangPhuc.ipynb` | Năm bước thực hành MLP theo tài liệu Lab 9. |
| `code/Baitaplab9.ipynb` | Lời giải bài tập 1–6, kết quả và giải thích cuối mỗi bài. |
| `data/xor.csv` | 400 điểm với `x1`, `x2` và nhãn `nhan`, dùng để học bài toán XOR mô phỏng. |
| `data/hai_vang_trang.csv` | 300 điểm, dùng khảo sát độ lớn mạng, điều chuẩn và hàm kích hoạt. |
| `data/sinh_vien_mo_rong.csv` | 120 sinh viên, dùng kiểm tra ảnh hưởng của chuẩn hóa các đặc trưng khác thang đo. |
| `data/gia_nha.csv` | 60 căn nhà, dùng so sánh MLPRegressor với hồi quy tuyến tính theo diện tích. |
| `figures/toc_do_hoc.png` | Bốn đường mất mát ứng với bốn tốc độ học ở bài tập 4. |
| `outputs/` | Hai file TXT chứa kết quả và thông báo lưu hình. |
| `scripts/run_all.py` | Chạy notebook thực hành rồi bài tập; cập nhật notebook và TXT. |
| `requirements.txt` | Các thư viện Python cần thiết. |
| `README.md` | Giới thiệu nội dung, cấu trúc và cách chạy. |

## 🛠️ Yêu cầu môi trường

Để chạy bài thực hành, cần cài đặt:  
Python 3.11 trở lên  
Jupyter Notebook hoặc Visual Studio Code có hỗ trợ notebook

Kiểm tra phiên bản Python bằng:

```text
python --version
```

Các phiên bản thư viện chưa được cố định trong `requirements.txt`. Kết quả huấn luyện có thể khác theo phiên bản scikit-learn, thư viện số và môi trường máy, dù đã đặt `random_state`. Ví dụ, lần chạy hiện tại của mạng `(100, 100)`, `alpha=1e-5` cho accuracy kiểm tra 0,8133, trong khi PDF minh họa 0,7333; mã vẫn giữ kiến trúc, tham số và cách chia dữ liệu theo đề.

## 📦 Cài đặt thư viện

### Cách 1 – Sử dụng `requirements.txt`

Từ thư mục `09. MLP`, chạy:

```text
python -m pip install -r requirements.txt
```

Nếu đang ở thư mục gốc repository, chạy:

```text
python -m pip install -r "09. MLP/requirements.txt"
```

### Cách 2 – Cài đặt thủ công qua cmd

```text
python -m pip install numpy pandas matplotlib scikit-learn notebook nbclient nbformat ipykernel jupyter-client matplotlib-inline pillow
```

## ▶️ Cách chạy bài thực hành

### Cách 1 - Khởi động Jupyter Notebook:

Từ thư mục `09. MLP`, chạy:

```text
jupyter notebook
```

Mở `code/Lab9_DoHoangPhuc.ipynb` hoặc `code/Baitaplab9.ipynb`, chạy ô **Chuẩn bị** rồi các cell từ trên xuống. Nếu CSV ở nơi khác, điền thư mục chứa dữ liệu vào `THU_MUC_DATA`. Trên Google Colab, tải các CSV lên theo yêu cầu. Bộ chữ số được nạp bằng `load_digits` có sẵn trong scikit-learn.

Chạy notebook trực tiếp sẽ hiển thị kết quả và lưu hình; để cập nhật hai file TXT, dùng script.

### Cách 2 - Chạy toàn bộ bằng script

Từ thư mục `09. MLP`, chạy:

```text
python scripts/run_all.py
```

Hoặc từ thư mục gốc repository:

```text
python "09. MLP/scripts/run_all.py"
```

Script dùng đúng Python đang gọi script và tạo kernel riêng cho từng notebook. Hai TXT được lưu trong `outputs/`; bài tập 4 lưu `figures/toc_do_hoc.png` và in thông báo lưu hình trong TXT.

Lab 9 có nhiều lần huấn luyện: phần thực hành kiểm định chéo điều chuẩn, bài tập 5 chạy 12 tổ hợp qua 5 fold và học lại mô hình tốt nhất. Vì vậy thời gian chạy phụ thuộc máy và có thể dài hơn các lab trước; script cho phép tối đa 7.200 giây mỗi cell.

Lưu thay đổi trong trình soạn thảo trước khi chạy vì script cập nhật notebook trên ổ đĩa. Sau khi sửa mã hoặc dữ liệu, chạy lại để notebook, TXT và hình phản ánh cùng kết quả.

## ⚠️ Lưu ý

### 1. Chạy từ thư mục gốc của Lab 9

Dùng thư mục `09. MLP`, hoặc các lệnh dành cho thư mục gốc repository đã ghi ở trên. Việc tìm CSV hỗ trợ mở notebook từ thư mục gốc repository, thư mục lab và `code/`.

### 2. Không thay đổi cấu trúc thư mục

Giữ `data/`, `figures/` và `outputs/`. Có thể dùng `THU_MUC_DATA` ở ô chuẩn bị hoặc tùy chọn `--data-dir` của script để chỉ định thư mục CSV thay thế. Đường dẫn có khoảng trắng phải đặt trong dấu nháy.

### 3. Cài đặt thư viện trước khi chạy

Nếu gặp `ModuleNotFoundError` hoặc thiếu `ipykernel_launcher`, cài thư viện vào đúng môi trường Python đang chạy script. Trong VS Code, chọn **Python: Select Interpreter**, mở terminal mới và chọn kernel tương ứng cho notebook.

Nếu xuất hiện `ConvergenceWarning`, mô hình có thể chưa hội tụ trong giới hạn tối ưu đã đặt. Đọc cảnh báo cùng số vòng và đường mất mát; việc chương trình hoàn tất không chứng minh nghiệm là tối ưu toàn cục.

Ở bài tập 5, scaler nằm trong pipeline và các tham số được chọn bằng CV trên tập học. Không thay tổ hợp theo điểm kiểm tra. Ở bài tập 6, dự đoán căn 250 m² vượt phạm vi diện tích học của dữ liệu hiện tại; đây là ngoại suy và chưa có giá thật để kiểm chứng mô hình nào đúng hơn.
