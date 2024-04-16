#جستجوی الگو با استفاده از گروه‌بندی
import re

# تعریف الگو با گروه‌بندی
pattern = r'(\d+)-(\d+)'

# جستجو با گروه‌بندی
result = re.search(pattern, 'From 123-456')

print(result.group(0))  # تمام الگو
print(result.group(1))  # گروه اول
print(result.group(2))  # گروه دوم
