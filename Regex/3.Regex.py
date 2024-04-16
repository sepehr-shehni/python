#جایگزینی الگوها در رشته
import re

# تعریف الگو
pattern = r'apple'

# جایگزینی تمامی الگوهای موجود در رشته
new_string = re.sub(pattern, 'orange', 'I have an apple and an apple tree')

print(new_string)
