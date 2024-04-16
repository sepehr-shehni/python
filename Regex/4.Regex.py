#جدا کردن رشته بر اساس الگو

import re

# تعریف الگو
pattern = r'\s+'

# جدا کردن رشته بر اساس فاصله
words = re.split(pattern, 'I have an apple')

print(words)
