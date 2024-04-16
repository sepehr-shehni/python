import tkinter as tk
import subprocess
import os

def execute_command():
    # گرفتن متن ورودی از ورودی کاربر
    command = entry.get()
    
    try:
        # اجرای دستور و دریافت خروجی آن
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # نمایش خروجی در ویجت Text
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, result.stdout)
        output_text.config(state=tk.DISABLED)

        output_label.config(text="دستور با موفقیت اجرا شد.")
    except Exception as e:
        output_label.config(text="خطایی رخ داده است: " + str(e))

def on_enter_press(event):
    execute_command()

# ساخت پنجره
root = tk.Tk()
root.title("اجرا کننده دستور")

# لیبل و ورودی متن
entry_label = tk.Label(root, text="دستور را وارد کنید:")
entry_label.pack(pady=6)
entry = tk.Entry(root, width=80)
entry.pack(pady=5)

# دکمه اجرا
execute_button = tk.Button(root, text="اجرا", command=execute_command)
execute_button.pack(pady=5)

# لیبل نتیجه
output_label = tk.Label(root, text="")
output_label.pack(pady=5)

# ویجت Text برای نمایش خروجی
output_text = tk.Text(root, wrap="word", height=10, state=tk.DISABLED)
output_text.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

# تابع کال‌بک برای وقتی که Enter زده شود
entry.bind("<Return>", on_enter_press)

root.mainloop()
