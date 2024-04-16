#تشخیص الگو در ابتدای یا انتهای رشته
import re

# تعریف الگو برای بررسی ابتدای رشته
pattern_start = r'^start'

# تعریف الگو برای بررسی انتهای رشته
pattern_end = r'end$'

# بررسی ابتدا و انتهای رشته
result_start = re.search(pattern_start, 'start of string')
result_end = re.search(pattern_end, 'string of end')

print(result_start)
print(result_end)
