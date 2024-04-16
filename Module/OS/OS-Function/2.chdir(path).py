import os

# نمایش مسیر کاری فعلی
print("Current working directory:", os.getcwd())

# تغییر مسیر کاری به "/path/to/new/directory"
os.chdir("E://")

# نمایش مسیر کاری جدید
print("New working directory:", os.getcwd())
