import re

def extract_passwords(file_path):
    # باز کردن فایل برای خواندن
    with open(file_path, 'r') as file:
        # خواندن محتوای فایل
        content = file.read()
        
        # تعریف الگو برای شناسایی پسوردها
        pattern = r'(?<=Password:\s)(\S+)'
        
        # جستجوی الگو در محتوای فایل
        passwords = re.findall(pattern, content)
        
        # چاپ پسوردهای یافت شده
        for password in passwords:
            print(password)

# فراخوانی تابع برای استخراج پسوردها از فایل متنی
extract_passwords('E:\\Project\\Python Project\\Regex\\file.txt')
