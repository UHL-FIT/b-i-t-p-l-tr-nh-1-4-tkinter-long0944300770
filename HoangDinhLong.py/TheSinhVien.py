import tkinter as tk

# Tạo cửa sổ
root = tk.Tk()
root.title("Thẻ Sinh Viên")
root.geometry("500x500")

# Đổi màu nền xám nhạt
root.configure(bg="#f8f9fa")

# Tiêu đề
label1 = tk.Label(
    root,
    text="THẺ SINH VIÊN",
    font=("Arial", 18, "bold"),
    bg="#f8f9fa",
    fg="blue"
)
label1.pack(pady=10)

# Thông tin sinh viên
label2 = tk.Label(
    root,
    text="Họ tên: Nguyễn Văn A",
    font=("Arial", 14),
    bg="#f8f9fa"
)
label2.pack(pady=5)

label3 = tk.Label(
    root,
    text="MSSV: 20240001",
    font=("Arial", 14),
    bg="#f8f9fa"
)
label3.pack(pady=5)

# Thêm khoa với màu xanh lá
label4 = tk.Label(
    root,
    text="Khoa: Công nghệ thông tin",
    font=("Arial", 14, "bold"),
    fg="green",
    bg="#f8f9fa"
)
label4.pack(pady=5)

# Nút đóng ứng dụng to hơn
btn = tk.Button(
    root,
    text="Đóng ứng dụng",
    font=("Arial", 14),
    width=15,   # chiều ngang nút
    height=2,   # chiều cao nút
    command=root.destroy
)
btn.pack(pady=20)

# Chạy chương trình
root.mainloop()