![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white) ![Jupyter Notebook](https://img.shields.io/badge/Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)

# Bài 1: Hồi quy tuyến tính

**Họ và tên:** Đỗ Hoàng Phúc  
**MSSV:** 24748020101313  
**Môn:** Học Máy Và Ứng Dụng  
**LHP:** 261_71ITAI41203_0101  
**GVHD:** ThS. Nguyễn Thái Anh ([GitHub](https://github.com/AnhNguyenVLU))  

## 📌 Nội dung bài thực hành

Lab 1 thực hành hồi quy tuyến tính trên dữ liệu gốc `gia_nha.csv` gồm 60 căn nhà. Nội dung gồm đọc dữ liệu, tính MSE, bình phương tối thiểu, hồi quy với scikit-learn, đánh giá bằng MAE/RMSE/R², Gradient Descent và hồi quy nhiều biến.

## 📂 Nội dung mã nguồn

- `code/Lab1_DoHoangPhuc.ipynb`: ô chuẩn bị và bảy bước thực hành theo tài liệu `Lab01_Hoi_quy_tuyen_tinh.pdf`, mỗi bước có cell mã và nhận xét.
- `code/Baitaplab1.ipynb`: ô chuẩn bị và sáu bài tập; cuối mỗi bài có `print` nhận xét, giải thích bằng tiếng Việt có dấu. Kết quả tính toán và nhãn hình dùng tiếng Việt không dấu.

Bài 4 tính lại R² của cả mô hình một biến và hai biến trên cùng tập kiểm tra, không gán sẵn điểm đối chiếu. Bài 5 giữ 200 vòng, thử hai tốc độ 0.001 và 1.02, có thêm 0.1 để đối chiếu. Bài 6 dùng lại đúng hệ số và khoảng diện tích của tài liệu theo yêu cầu đề, không huấn luyện lại.

## 📁 Cấu trúc thư mục

```text
01. Linear_Regression/
├── code/
│   ├── Baitaplab1.ipynb
│   └── Lab1_DoHoangPhuc.ipynb
├── data/
│   └── gia_nha.csv
├── figures/
│   ├── bai2.png
│   └── bai3_tuoi_nha.png
├── outputs/
│   ├── Baitaplab1.txt
│   └── Lab1_DoHoangPhuc.txt
├── scripts/
│   └── run_all.py
├── README.md
└── requirements.txt
```

| Thư mục / tệp | Chức năng |
| --- | --- |
| `code/` | Hai notebook thực hành và bài tập, chạy cell từ trên xuống. |
| `data/` | Chứa dataset gốc; các cột là `dien_tich`, `so_phong`, `tuoi_nha`, `gia`. |
| `figures/` | Ảnh do notebook sinh ra, lưu trực tiếp vào đây trước khi hiển thị. |
| `outputs/` | Nhật ký chữ của từng notebook, gồm kết quả và nhận xét đã in. |
| `scripts/run_all.py` | Chạy notebook thực hành trước, bài tập sau; cập nhật notebook và nhật ký. |
| `requirements.txt` | Các thư viện dùng cho tính toán, biểu đồ và chạy notebook. |
| `README.md` | Nội dung lab, cấu trúc, cài đặt và cách chạy. |

## 🛠️ Yêu cầu môi trường

Dùng Python 3. Nếu mở notebook trực tiếp, dùng Jupyter Notebook hoặc VS Code có hỗ trợ notebook. Script chạy chung dùng đúng Python đang gọi script để tạo kernel riêng cho mỗi notebook.

Hai notebook đã được chạy thử riêng lẻ và chạy qua `scripts/run_all.py` trên máy người thực hiện, tạo đủ các tệp kết quả. Khi chạy trên máy khác, cần cài đầy đủ thư viện và chuẩn bị dữ liệu theo hướng dẫn dưới đây. Phiên bản Python và thư viện khác nhau có thể ảnh hưởng đến khả năng tương thích hoặc cách hiển thị kết quả.

## 📦 Cài đặt thư viện

Mở terminal tại thư mục `01. Linear_Regression` rồi chạy:

```sh
python -m pip install -r requirements.txt
```

Nên cài trong một môi trường Python riêng cho bài thực hành. Khi mở notebook, chọn kernel của đúng môi trường đã cài thư viện. Nếu gặp `ModuleNotFoundError`, kiểm tra lại môi trường đang dùng và chạy lại lệnh cài đặt trên. Tệp `requirements.txt` liệt kê các thư viện cần thiết, chưa cố định phiên bản cụ thể.

## ▶️ Cách chạy bài thực hành

### Cách 1 — Chạy toàn bộ bằng script

Tại thư mục `01. Linear_Regression`, chạy:

```sh
python scripts/run_all.py
```

Nếu dataset nằm ở nơi khác, chỉ định đường dẫn, đặt trong dấu nháy khi có khoảng trắng:

```sh
python scripts/run_all.py --data "D:/Du lieu/gia_nha.csv"
```

Có thể gọi script bằng đường dẫn tuyệt đối từ thư mục khác. Với `--data`, đường dẫn tương đối được tính từ nơi mở terminal. Khi chạy bằng script, ảnh luôn lưu về `figures/` của Lab 1, dù CSV nằm ngoài lab.

Script dùng `nbclient` để thực thi thật các cell, lưu notebook khi chạy thành công và ghi nhật ký riêng cho từng notebook vào `outputs/`. Nếu có lỗi, script dừng và ghi phần kết quả đã có vào nhật ký để tra cứu. File nhật ký chỉ chứa văn bản và dòng đánh dấu biểu đồ; ảnh xem trong notebook hoặc `figures/`.

### Cách 2 — Mở notebook trực tiếp

```sh
jupyter notebook
```

Mở một trong hai notebook trong `code/`. Chạy ô **Chuẩn bị** trước, sau đó các bước hoặc bài tập theo thứ tự. Khi đang đứng ở gốc lab, gốc repository hoặc thư mục `code/`, ô chuẩn bị tìm dữ liệu ở những vị trí tương đối tương ứng.

Nếu dataset nằm ở vị trí khác, sửa dòng trong ô chuẩn bị thành đường dẫn thực tế, ví dụ:

```python
DUONG_DAN_DATASET = "D:/Du lieu/gia_nha.csv"
```

File được chỉ định phải tồn tại, nếu không chương trình báo rõ đường dẫn lỗi. Khi để trống, chương trình thử tìm đúng tên `gia_nha.csv` trong `data/`, thư mục hiện tại và các vị trí tương đối thông dụng; không tìm trên toàn bộ ổ đĩa.

### Cách 3 — Google Colab

Tải notebook trong `code/` lên Colab và chạy ô chuẩn bị. Nếu chưa có dataset, chương trình yêu cầu tải lên `gia_nha.csv`. Cũng có thể gán `DUONG_DAN_DATASET` tới một file đã có trong phiên Colab. Chạy tiếp các cell từ trên xuống; ảnh lưu vào `figures/` trong thư mục làm việc của phiên Colab.

## ⚠️ Lưu ý

- Tải đầy đủ thư mục Lab 1, đặc biệt là hai notebook trong `code/` và dữ liệu gốc `data/gia_nha.csv`. Nếu đặt CSV ở nơi khác, dùng `--data` hoặc chỉ định `DUONG_DAN_DATASET` như hướng dẫn ở trên.
- Các lệnh trong README được viết để chạy từ thư mục `01. Linear_Regression`. Khi chạy notebook trực tiếp, chạy ô chuẩn bị trước và kiểm tra đường dẫn dataset được in ra.
- Giữ nguyên dữ liệu gốc khi đối chiếu kết quả với tài liệu.
- Giữ `test_size=0.2` và `random_state=42` ở các phần so sánh mô hình.
- Chạy lại `scripts/run_all.py` sau khi thay đổi mã hoặc dữ liệu để cập nhật kết quả trong notebook, hai file TXT trong `outputs/` và ảnh trong `figures/`.
- Nhật ký `.txt` và hình PNG không thay thế ảnh chụp màn hình phần kết quả mà đề yêu cầu nộp.
