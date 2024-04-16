import tkinter as tk
from tkinter import filedialog
import os
from zipfile import ZipFile

def create_folder_and_zip():
    # دریافت مسیر انتخابی از کاربر
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return  # اگر کاربر لغو کرد، خروج

    # ایجاد فولدر در مسیر انتخابی
    folder_name = "my_folder"
    folder_path = os.path.join(folder_path, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # ایجاد چند فایل نمونه درون فولدر
    for i in range(3):
        with open(os.path.join(folder_path, f"file_{i}.txt"), "w") as f:
            f.write(f"This is file {i}")

    # فشرده‌سازی فولدر
    zip_file_path = os.path.join(os.path.dirname(folder_path), f"{folder_name}.zip")
    with ZipFile(zip_file_path, "w") as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)

    # نمایش پیام موفقیت‌آمیز به کاربر
    tk.messagebox.showinfo("Success", f"Folder '{folder_name}' created and zipped successfully at:\n{zip_file_path}")

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("Folder Creator & Zipper")

# ایجاد دکمه برای اجرای عملیات
create_button = tk.Button(root, text="Create Folder & Zip", command=create_folder_and_zip)
create_button.pack(padx=20, pady=10)

# اجرای برنامه
root.mainloop()
