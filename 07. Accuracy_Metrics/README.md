![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white) ![Jupyter Notebook](https://img.shields.io/badge/Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)

# Bài 7: Đánh giá mô hình

**Họ và tên:** Đỗ Hoàng Phúc  
**MSSV:** 24748020101313  
**Môn:** Học Máy Và Ứng Dụng  
**LHP:** 261_71ITAI41203_0101  
**GVHD:** ThS. Nguyễn Thái Anh ([GitHub](https://github.com/AnhNguyenVLU))  

## 📌 Nội dung bài thực hành

Bài thực hành tìm hiểu cách **đánh giá mô hình trên dữ liệu lệch lớp**, sử dụng dữ liệu mô phỏng 1.200 sinh viên để phát hiện nguy cơ bỏ học. Phần bài tập còn sử dụng dữ liệu giá nhà và bộ chữ số viết tay có sẵn trong scikit-learn.

Nội dung bao gồm:

* So sánh hồi quy logistic với mô hình lười luôn đoán lớp đông nhất
* Tự đếm TP, FP, FN, TN và đọc ma trận nhầm lẫn
* Tính accuracy, precision, recall và F1 bằng tay và bằng thư viện
* Đọc báo cáo phân loại và phân biệt macro avg với weighted avg
* Thay đổi ngưỡng xác suất và chọn ngưỡng bằng kiểm định chéo trên tập học
* Đánh giá khả năng xếp hạng bằng đường ROC và AUC
* So sánh các mô hình đã học, kiểm định chéo nhiều thước đo và cân bằng lớp
* Thực hiện sáu bài tập, gồm phân tích chữ số, vẽ ROC và khảo sát ảnh hưởng của sai số lớn tới MAE, RMSE và R²

## 📂 Nội dung mã nguồn

Hai notebook chính được sử dụng trong bài:

`code/Lab7_DoHoangPhuc.ipynb`

Notebook thực hiện sáu bước theo tài liệu Lab 7: accuracy trên dữ liệu lệch lớp, ma trận nhầm lẫn, precision–recall–F1, ngưỡng quyết định, ROC–AUC, kiểm định chéo và cân bằng lớp. Mỗi bước có cell mã riêng; ô chuẩn bị hỗ trợ tìm CSV khi mở notebook từ các thư mục làm việc khác nhau.

`code/Baitaplab7.ipynb`

Notebook chứa lời giải sáu bài tập, kết quả tính toán và phần nhận xét, giải thích bằng tiếng Việt có dấu ở cuối mỗi bài. Nhãn kết quả tính toán dùng tiếng Việt không dấu. Bài 1 giải thích kỹ các ô của ma trận nhầm lẫn và quy ước chia cho 0; bài 3 giải thích cách chọn ngưỡng mà không dùng nhãn tập kiểm tra.

## 📁 Cấu trúc thư mục

```text
07. Accuracy_Metrics/
├── code/
│   ├── Baitaplab7.ipynb
│   └── Lab7_DoHoangPhuc.ipynb
├── data/
│   ├── gia_nha.csv
│   └── sinh_vien_bo_hoc.csv
├── figures/
│   └── roc.png
├── outputs/
│   ├── Baitaplab7.txt
│   └── Lab7_DoHoangPhuc.txt
├── scripts/
│   └── run_all.py
├── README.md
└── requirements.txt
```

| Thư mục / tệp | Chức năng |
| --- | --- |
| `code/` | Chứa hai notebook. Chạy ô chuẩn bị trước, sau đó chạy các cell theo thứ tự. |
| `code/Lab7_DoHoangPhuc.ipynb` | Sáu bước thực hành đánh giá mô hình theo tài liệu Lab 7. |
| `code/Baitaplab7.ipynb` | Lời giải bài tập 1–6 với kết quả và giải thích cuối mỗi bài. |
| `data/sinh_vien_bo_hoc.csv` | 1.200 sinh viên với các đặc trưng `diem_tb`, `so_buoi_vang`, `tin_chi_no`, `gio_lam_them` và nhãn `bo_hoc`. |
| `data/gia_nha.csv` | 60 căn nhà với diện tích, số phòng, tuổi nhà và giá tính bằng tỷ đồng; dùng cho bài tập 6. |
| `figures/roc.png` | Đường ROC của hồi quy logistic và rừng ngẫu nhiên trong bài tập 4. |
| `outputs/` | Kết quả dạng văn bản của hai notebook, gồm các thông báo lưu hình. |
| `scripts/run_all.py` | Chạy notebook thực hành rồi notebook bài tập; cập nhật notebook và hai file TXT. |
| `requirements.txt` | Danh sách thư viện Python cần thiết. |
| `README.md` | Giới thiệu nội dung, cấu trúc và cách chạy bài thực hành. |

## 🛠️ Yêu cầu môi trường

Để chạy bài thực hành, cần cài đặt:  
Python 3.11 trở lên; bài đã được chạy kiểm tra bằng Python 3.12.10  
Jupyter Notebook hoặc Visual Studio Code có hỗ trợ notebook

Có thể kiểm tra phiên bản Python bằng:

```text
python --version
```

Phiên bản Python và thư viện khác nhau có thể làm thay đổi kết quả ở các chữ số cuối. `requirements.txt` giới hạn scikit-learn dưới 1.11 để giữ cách dùng `SVC(probability=True)` của tài liệu; các thư viện còn lại chưa cố định phiên bản.

## 📦 Cài đặt thư viện

### Cách 1 – Sử dụng `requirements.txt`

Từ thư mục `07. Accuracy_Metrics`, chạy:

```text
python -m pip install -r requirements.txt
```

Nếu đang ở thư mục gốc repository, chạy:

```text
python -m pip install -r "07. Accuracy_Metrics/requirements.txt"
```

### Cách 2 – Cài đặt thủ công qua cmd

```text
python -m pip install numpy pandas matplotlib "scikit-learn<1.11" notebook nbclient nbformat ipykernel jupyter-client matplotlib-inline
```

## ▶️ Cách chạy bài thực hành

### Cách 1 - Khởi động Jupyter Notebook:

Từ thư mục `07. Accuracy_Metrics`, chạy:

```text
jupyter notebook
```

Mở `code/Lab7_DoHoangPhuc.ipynb` hoặc `code/Baitaplab7.ipynb`, chọn đúng kernel, chạy ô **Chuẩn bị** rồi các cell từ trên xuống. Nếu CSV ở nơi khác, điền đường dẫn vào `DUONG_DAN_SINH_VIEN` và `DUONG_DAN_GIA_NHA` trong ô chuẩn bị. Trên Google Colab, tải CSV lên khi notebook yêu cầu; bộ chữ số được nạp từ scikit-learn.

Chạy notebook trực tiếp sẽ hiển thị kết quả; để cập nhật hai file TXT, chạy script bên dưới.

### Cách 2 - Chạy toàn bộ bằng script

Từ thư mục `07. Accuracy_Metrics`, chạy:

```text
python scripts/run_all.py
```

Hoặc từ thư mục gốc repository:

```text
python "07. Accuracy_Metrics/scripts/run_all.py"
```

Script dùng chính Python đang gọi script để khởi động kernel riêng cho từng notebook. Kết quả dạng chữ được lưu vào hai file TXT trong `outputs/`; bài tập 4 lưu `figures/roc.png` và in `Da luu hinh: figures/roc.png`. Thông báo lỗi được hiển thị trong terminal.

Lưu các chỉnh sửa trong trình soạn thảo trước khi chạy script vì script cập nhật notebook trên ổ đĩa. Sau khi sửa mã hoặc dữ liệu, chạy lại để notebook, TXT và hình phản ánh cùng kết quả.

## ⚠️ Lưu ý

### 1. Chạy từ thư mục gốc của Lab 7

Nên chạy các lệnh từ `07. Accuracy_Metrics`, hoặc dùng các lệnh dành cho thư mục gốc repository đã ghi ở trên. Cách tìm dữ liệu hỗ trợ mở notebook từ thư mục gốc repository, thư mục lab và `code/`.

### 2. Không thay đổi cấu trúc thư mục

Giữ các thư mục `data/`, `figures/` và `outputs/`. Nếu CSV nằm nơi khác, ngoài cách chỉ định trong ô chuẩn bị, có thể dùng tùy chọn `--sinh-vien` và `--gia-nha` của script; đường dẫn có khoảng trắng phải đặt trong dấu nháy.

### 3. Cài đặt thư viện trước khi chạy

Nếu gặp `ModuleNotFoundError` hoặc `No module named ipykernel_launcher`, cài lại thư viện vào đúng môi trường Python đang chạy script. Trong VS Code, dùng **Python: Select Interpreter** để chọn môi trường đã cài và mở terminal mới; kernel của notebook cũng phải dùng môi trường có đủ thư viện.

Một số phiên bản scikit-learn hiển thị `FutureWarning` với `SVC(probability=True)`. Mã giữ cách tính xác suất trong PDF để tiện đối chiếu; cảnh báo này không phải lỗi thực thi.

Ở bước 4 thực hành, bảng thử ngưỡng trên tập kiểm tra dùng để minh họa. Ngưỡng chính thức được chọn bằng dự đoán ngoài fold trên tập học; bài tập 3 cũng giữ nguyên nguyên tắc này. Không điều chỉnh lại ngưỡng theo nhãn kiểm tra sau khi xem kết quả.
