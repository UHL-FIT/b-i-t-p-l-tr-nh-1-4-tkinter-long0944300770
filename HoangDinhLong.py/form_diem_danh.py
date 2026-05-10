import tkinter as tk

# Tạo cửa sổ
root = tk.Tk()
root.title("Quản lý Sinh viên - UHL")
root.geometry("500x500")

# Chỉ cho cột ô nhập liệu co giãn
root.columnconfigure(1, weight=1)

# Tạo các thành phần
nhan_ma_sv = tk.Label(root, text="Mã sinh viên:")
o_nhap_ma_sv = tk.Entry(root)

nhan_ho_ten = tk.Label(root, text="Họ và tên:")
o_nhap_ho_ten = tk.Entry(root)

# Hiển thị dòng Mã sinh viên
nhan_ma_sv.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky="w"
)

o_nhap_ma_sv.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky="ew"
)

# Hiển thị dòng Họ và tên
nhan_ho_ten.grid(
    row=1,
    column=0,
    padx=10,
    pady=10,
    sticky="w"
)

o_nhap_ho_ten.grid(
    row=1,
    column=1,
    padx=10,
    pady=10,
    sticky="ew"
)

# Chạy chương trình
root.mainloop()