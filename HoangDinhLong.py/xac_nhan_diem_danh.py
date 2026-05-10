import tkinter as tk
from tkinter import messagebox
from datetime import datetime


# Hàm xử lý dữ liệu
def xu_ly_du_lieu():

    # Lấy dữ liệu
    mssv = o_nhap_ma_sv.get()
    ho_ten = o_nhap_ho_ten.get()

    # In thời gian ra terminal
    thoi_gian = datetime.now().strftime("%H:%M:%S")

    print(f"[{thoi_gian}] Đã nhấn: MSSV {mssv} - Tên: {ho_ten}")

    # Kiểm tra rỗng
    if mssv == "" or ho_ten == "":
        messagebox.showerror(
            "Chú ý",
            "Vui lòng không để trống thông tin sinh viên!"
        )
        return

    # Kiểm tra MSSV phải là số
    if not mssv.isdigit():
        messagebox.showerror(
            "Lỗi",
            "Mã sinh viên chỉ được nhập số!"
        )
        return

    # Thành công
    nhan_ket_qua.config(
        text=f"Thành công: Đã nhận dữ liệu của {ho_ten}",
        fg="green"
    )

    # Xóa trắng ô nhập
    o_nhap_ma_sv.delete(0, tk.END)
    o_nhap_ho_ten.delete(0, tk.END)


# Tạo cửa sổ
root = tk.Tk()
root.title("Quản lý Sinh viên - UHL")
root.geometry("400x350")

# Cho ô nhập co giãn
root.columnconfigure(1, weight=1)


# ===== Giao diện =====

tk.Label(root, text="Mã sinh viên:").grid(
    row=0, column=0,
    padx=10, pady=10,
    sticky="w"
)

o_nhap_ma_sv = tk.Entry(root)
o_nhap_ma_sv.grid(
    row=0, column=1,
    padx=10, pady=10,
    sticky="ew"
)


tk.Label(root, text="Họ và tên:").grid(
    row=1, column=0,
    padx=10, pady=10,
    sticky="w"
)

o_nhap_ho_ten = tk.Entry(root)
o_nhap_ho_ten.grid(
    row=1, column=1,
    padx=10, pady=10,
    sticky="ew"
)


# Nút bấm
nut_xac_nhan = tk.Button(
    root,
    text="Xác nhận điểm danh",
    command=xu_ly_du_lieu
)

nut_xac_nhan.grid(
    row=2,
    column=0,
    columnspan=2,
    pady=10
)


# Label kết quả
nhan_ket_qua = tk.Label(
    root,
    text="Hệ thống sẵn sàng",
    font=("Arial", 10, "italic")
)

nhan_ket_qua.grid(
    row=3,
    column=0,
    columnspan=2,
    pady=20
)


root.mainloop()