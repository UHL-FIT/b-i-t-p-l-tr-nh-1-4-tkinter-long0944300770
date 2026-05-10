import tkinter as tk

# Tạo cửa sổ
root = tk.Tk()

# Đổi tiêu đề cửa sổ thành tên của tôi
root.title("mở đầu")

# Đổi kích thước từ 400x200 thành 500x500
root.geometry("500x500")

# Dòng chữ chào mừng
label = tk.Label(
    root,
    text="Tôi tên là Hoàng Đình Long",
    font=("Arial", 16)
)

# Hiển thị ở giữa cửa sổ
label.pack(expand=True)

# Chạy chương trình
root.mainloop()