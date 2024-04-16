#جستجوی الگو با استفاده از lookaround
import re

# تعریف الگو با lookaround
pattern = r'(?<=@)\w+'

# جستجو با استفاده از lookaround
result = re.search(pattern, 'Email: example@mail.com')

print(result.group())
