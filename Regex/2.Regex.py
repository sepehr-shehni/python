#جستجوی یک الگو در تمامی رشته
import re

# تعریف الگو
pattern = r'apple'

# جستجوی تمامی الگوهای موجود در رشته
result = re.findall(pattern, 'I have an apple and an apple tree')

print(result)
