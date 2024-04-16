#جستجوی یک الگو با تعداد تکرار مشخص
import re

# تعریف الگو برای یک عدد تکراری
pattern = r'\d{3}'

# جستجوی الگو با تعداد تکرار مشخص
result = re.search(pattern, '123456')

print(result.group())
