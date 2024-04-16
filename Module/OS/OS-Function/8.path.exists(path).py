import os

path_to_check = "E://test"

# بررسی وجود مسیر
if os.path.exists(path_to_check):
    print("Path exists.")
else:
    print("Path does not exist.")
