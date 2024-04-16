#استفاده از الگوی بیشتر
import re

# تعریف الگو برای جستجوی آدرس ایمیل
pattern = r'[\w\.-]+@[\w\.-]+'

# جستجوی آدرس ایمیل در رشته
result = re.findall(pattern, 'Emails: example@mail.com, test@example.com')

print(result)
