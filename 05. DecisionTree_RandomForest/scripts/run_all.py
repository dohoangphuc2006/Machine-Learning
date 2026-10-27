"""Chạy các notebook trong code/, lưu kết quả và nhật ký bằng một lệnh."""

import json
import os
from pathlib import Path
import sys
import tempfile


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
                    cac_doan.append("[Biểu đồ hiển thị trong notebook]\n")
                elif "text/plain" in noi_dung:
                    cac_doan.append(noi_dung["text/plain"] + "\n")
            elif ket_qua.output_type == "error":
                cac_doan.append(f"{ket_qua.ename}: {ket_qua.evalue}\n")
        cac_doan.append("\n")
    duong_dan.write_text("".join(cac_doan), encoding="utf-8")


def main():
    if Path(__file__).resolve().parent.name == "scripts":
        thu_muc_du_an = Path(__file__).resolve().parents[1]
    else:
        thu_muc_du_an = Path(__file__).resolve().parent

    thu_muc_ket_qua = thu_muc_du_an / "outputs"
    cac_notebook = sorted(
        (thu_muc_du_an / "code").glob("*.ipynb"),
        key=lambda p: (not p.name.lower().startswith("lab"), p.name.lower()),
    )
    if not cac_notebook:
        print("Không tìm thấy notebook trong thư mục code/.", file=sys.stderr)
        return 1

    tep_du_lieu_can_thiet = [
        thu_muc_du_an / "data" / "khach_vay.csv",
        thu_muc_du_an / "data" / "gia_nha.csv",
    ]
    for tep in tep_du_lieu_can_thiet:
        if not tep.is_file():
            print(
                f"Thiếu file dữ liệu: {tep.name}. Hãy kiểm tra thư mục data/.",
                file=sys.stderr,
            )
            return 1

    try:
        from jupyter_client import KernelManager
        from jupyter_client.kernelspec import KernelSpecManager
        from nbclient import NotebookClient
        import nbformat
    except ImportError:
        print("Chưa đủ thư viện. Cài bằng lệnh sau rồi chạy lại:", file=sys.stderr)
        print(
            f'"{sys.executable}" -m pip install -r "{thu_muc_du_an / "requirements.txt"}"',
            file=sys.stderr,
        )
        return 1

    thu_muc_ket_qua.mkdir(exist_ok=True)
    (thu_muc_du_an / "figures").mkdir(exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="cay_quyet_dinh_kernel_") as tam:
        thu_muc_kernel = Path(tam) / "python3"
        thu_muc_kernel.mkdir()
        cau_hinh = {
            "argv": [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
            "display_name": "Python 3",
            "language": "python",
            "env": {"MPLBACKEND": "module://matplotlib_inline.backend_inline"},
        }
        (thu_muc_kernel / "kernel.json").write_text(json.dumps(cau_hinh), encoding="utf-8")

        for duong_dan in cac_notebook:
            print(f"Đang chạy: {duong_dan.name}", flush=True)
            notebook = nbformat.read(duong_dan, as_version=4)

            nhat_ky = thu_muc_ket_qua / f"{duong_dan.stem}.txt"
            quan_ly_kernel = KernelManager(
                kernel_name="python3",
                kernel_spec_manager=KernelSpecManager(kernel_dirs=[tam]),
            )
            try:
                NotebookClient(
                    notebook,
                    km=quan_ly_kernel,
                    timeout=600,
                    resources={"metadata": {"path": str(thu_muc_du_an)}},
                ).execute(cleanup_kc=True)
            except Exception as loi:
                ghi_nhat_ky(notebook, nhat_ky)
                print(f"Lỗi khi chạy {duong_dan.name}: {loi}", file=sys.stderr)
                print(f"Xem nhật ký: {nhat_ky}", file=sys.stderr)
                return 1

            ban_tam = duong_dan.with_suffix(".ipynb.tmp")
            nbformat.write(notebook, ban_tam)
            os.replace(ban_tam, duong_dan)
            ghi_nhat_ky(notebook, nhat_ky)
            print(f"  Đã lưu notebook và outputs/{nhat_ky.name}", flush=True)

    # Tự động di chuyển các file ảnh nếu notebook lưu tại thư mục gốc
    for tep_anh in thu_muc_du_an.glob("*.png"):
        dich_den = thu_muc_du_an / "figures" / tep_anh.name
        if dich_den.is_file():
            dich_den.unlink()
        tep_anh.rename(dich_den)

    print()
    print("Hoàn tất tất cả notebook.")
    return 0


if __name__ == "__main__":
    for luong in (sys.stdout, sys.stderr):
        if hasattr(luong, "reconfigure"):
            luong.reconfigure(encoding="utf-8")
    raise SystemExit(main())
