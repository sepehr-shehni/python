#جستجوی الگو در یک رشته:
import re

# تعریف الگو
pattern = r'apple'

# جستجو در رشته
result = re.search(pattern, 'I have an apple')

print(result.group())
