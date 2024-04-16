#استفاده از lookbehind و lookahead
import re

# تعریف الگو با lookbehind و lookahead
pattern = r'(?<=@)[\w\.]+(?=\.\w+)'

# جستجو با استفاده از lookbehind و lookahead
result = re.findall(pattern, 'Emails: example@mail.com, test@example.com')

print(result)
