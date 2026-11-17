"""Chạy các notebook trong code/, lưu kết quả và nhật ký bằng một lệnh."""

import argparse
import importlib.util
import json
import os
from pathlib import Path
import re
import sys
import tempfile


def an_duong_dan_ca_nhan(noi_dung):
    """Ẩn thư mục lab và thư mục người dùng trong thông báo lỗi."""
    for thu_muc, thay_the in (
        (Path(__file__).resolve().parents[1], "."),
        (Path.home(), "<thu_muc_nguoi_dung>"),
    ):
        for duong_dan in sorted(
            {str(thu_muc), thu_muc.as_posix(), str(thu_muc).replace("\\", "\\\\")},
            key=len, reverse=True,
        ):
            noi_dung = re.sub(re.escape(duong_dan), lambda _: thay_the, noi_dung,
                              flags=re.IGNORECASE if os.name == "nt" else 0)
    return noi_dung


def ghi_nhat_ky(notebook, duong_dan):
    """Lưu phần kết quả dạng chữ; hình vẫn nằm trong notebook và figures/."""
    cac_doan = []
    for so_cell, cell in enumerate(notebook.cells, start=1):
        if cell.cell_type != "code":
            continue
        cac_doan.append(f"--- Cell {so_cell} ---\n")
        for ket_qua in cell.get("outputs", []):
            if ket_qua.output_type == "stream":
                cac_doan.append(ket_qua.text)
            elif ket_qua.output_type in ("execute_result", "display_data"):
                noi_dung = ket_qua.get("data", {})
                if "image/png" in noi_dung:
                    cac_doan.append("[Bieu do hien thi trong notebook]\n")
                elif "text/plain" in noi_dung:
                    cac_doan.append(noi_dung["text/plain"] + "\n")
            elif ket_qua.output_type == "error":
                cac_doan.append(f"{ket_qua.ename}: {ket_qua.evalue}\n")
        cac_doan.append("\n")
    duong_dan.write_text(an_duong_dan_ca_nhan("".join(cac_doan)), encoding="utf-8")


def kiem_tra_thu_vien():
    """Kiểm tra ngay Python dùng cho script, cũng là Python dùng cho kernel."""
    cac_module = {
        "ipykernel_launcher": "ipykernel", "nbformat": "nbformat",
        "nbclient": "nbclient", "jupyter_client": "jupyter-client",
        "matplotlib_inline": "matplotlib-inline", "numpy": "numpy",
        "pandas": "pandas", "matplotlib": "matplotlib", "sklearn": "scikit-learn",
        "PIL": "pillow",
    }
    thieu = [goi for module, goi in cac_module.items()
             if importlib.util.find_spec(module) is None]
    if not thieu:
        return True
    print("Python dang chay script thieu thu vien: " + ", ".join(thieu), file=sys.stderr)
    print("Trong VS Code: Python: Select Interpreter -> chon dung moi truong da cai thu vien.",
          file=sys.stderr)
    print("Mo terminal cua moi truong do, tu thu muc goc repository chay:", file=sys.stderr)
    print('python -m pip install -r "08. K-Means/requirements.txt"', file=sys.stderr)
    return False


def main():
    phan_tich = argparse.ArgumentParser(
        description="Chay hai notebook Lab 8, luu ket qua vao outputs va anh vao figures."
    )
    phan_tich.add_argument("--data-dir", type=Path, help="Thu muc du lieu thay the.")
    tham_so = phan_tich.parse_args()
    if not kiem_tra_thu_vien():
        return 1
    # Dựa vào vị trí script, không phụ thuộc nơi người dùng mở terminal.
    thu_muc_du_an = Path(__file__).resolve().parents[1]
    thu_muc_ket_qua = thu_muc_du_an / "outputs"
    cac_notebook = sorted(
        (thu_muc_du_an / "code").glob("*.ipynb"),
        key=lambda p: (not p.name.lower().startswith("lab"), p.name.lower()),
    )
    if not cac_notebook:
        print("Khong tim thay notebook trong thu muc code/.", file=sys.stderr)
        return 1
    du_lieu_chi_dinh = tham_so.data_dir or os.environ.get("LAB8_DATA_DIR", "")
    if du_lieu_chi_dinh and not Path(du_lieu_chi_dinh).is_dir():
        print("Khong tim thay thu muc du lieu chi dinh.", file=sys.stderr)
        return 1
    du_lieu_chi_dinh = str(Path(du_lieu_chi_dinh).resolve()) if du_lieu_chi_dinh else ""

    try:
        import nbformat
        from nbclient import NotebookClient
        from jupyter_client import KernelManager
        from jupyter_client.kernelspec import KernelSpecManager
    except ImportError:
        print("Chua du thu vien. Cai bang lenh sau roi chay lai:", file=sys.stderr)
        print("Tu thu muc lab, chay: python -m pip install -r requirements.txt", file=sys.stderr)
        return 1

    thu_muc_ket_qua.mkdir(exist_ok=True)
    (thu_muc_du_an / "figures").mkdir(exist_ok=True)

    # Kernel tạm dùng đúng Python đang chạy script, không đổi cấu hình Jupyter.
    with tempfile.TemporaryDirectory(prefix="lab8_kernel_") as tam:
        thu_muc_kernel = Path(tam) / "python3"
        thu_muc_kernel.mkdir()
        bien_moi_truong = {
            "MPLBACKEND": "module://matplotlib_inline.backend_inline",
            "LAB8_ROOT": str(thu_muc_du_an),
            "LAB8_DATA_DIR": du_lieu_chi_dinh,
        }
        cau_hinh = {
            "argv": [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
            "display_name": "Python 3",
            "language": "python",
            "env": bien_moi_truong,
        }
        (thu_muc_kernel / "kernel.json").write_text(json.dumps(cau_hinh), encoding="utf-8")

        for duong_dan in cac_notebook:
            print(f"Dang chay: {duong_dan.name}", flush=True)
            notebook = nbformat.read(duong_dan, as_version=4)
            # Ô chuẩn bị tự tìm dữ liệu; script không sửa mã của notebook.
            nhat_ky = thu_muc_ket_qua / f"{duong_dan.stem}.txt"
            quan_ly_kernel = KernelManager(
                kernel_name="python3",
                kernel_spec_manager=KernelSpecManager(kernel_dirs=[tam]),
            )
            try:
                # Mỗi notebook có kernel riêng; dừng nếu một cell báo lỗi.
                NotebookClient(
                    notebook,
                    km=quan_ly_kernel,
                    timeout=7200,
                    resources={"metadata": {"path": str(thu_muc_du_an)}},
                ).execute(cleanup_kc=True)
            except Exception as loi:
                ghi_nhat_ky(notebook, nhat_ky)
                print(an_duong_dan_ca_nhan(f"Loi khi chay {duong_dan.name}: {loi}"), file=sys.stderr)
                print(f"Xem nhat ky: outputs/{nhat_ky.name}", file=sys.stderr)
                return 1

            # Ẩn đường dẫn trong cả output notebook, ngoài nhật ký TXT và terminal.
            for cell in notebook.cells:
                for ket_qua in cell.get("outputs", []):
                    if "text" in ket_qua:
                        ket_qua.text = an_duong_dan_ca_nhan(ket_qua.text)
                    for kieu, noi_dung in ket_qua.get("data", {}).items():
                        if kieu.startswith("text/") and isinstance(noi_dung, str):
                            ket_qua.data[kieu] = an_duong_dan_ca_nhan(noi_dung)
            # Chỉ cập nhật notebook gốc khi toàn bộ cell đã chạy thành công.
            print(f"Dang luu ket qua: {duong_dan.name}", flush=True)
            ban_tam = duong_dan.with_suffix(".ipynb.tmp")
            nbformat.write(notebook, ban_tam)
            os.replace(ban_tam, duong_dan)
            ghi_nhat_ky(notebook, nhat_ky)
            print(f"  Da luu notebook va outputs/{nhat_ky.name}", flush=True)

    print(f"Hoan tat {len(cac_notebook)} notebook. Thu muc bieu do: figures/")
    return 0


def chay_script():
    # Hiển thị tiếng Việt trên terminal Windows.
    for luong in (sys.stdout, sys.stderr):
        if hasattr(luong, "reconfigure"):
            luong.reconfigure(encoding="utf-8")
    print(f"Lab 8 | Python {sys.version.split()[0]}", flush=True)
    try:
        return main()
    except Exception as loi:
        print(an_duong_dan_ca_nhan(f"Loi chay script ({type(loi).__name__}): {loi}"), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(chay_script())
