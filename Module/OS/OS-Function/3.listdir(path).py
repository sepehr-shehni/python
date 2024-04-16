import os

# مسیری که می‌خواهیم فایل‌ها و دایرکتوری‌های آن را بررسی کنیم
path_to_check = "E://"

# دریافت لیست فایل‌ها و دایرکتوری‌ها
files_and_dirs = os.listdir(path_to_check)
#print(type(files_and_dirs))
# چاپ لیست فایل‌ها و دایرکتوری‌ها
print("Files and directories in", path_to_check, "are:")
for item in files_and_dirs:
    print(item)
