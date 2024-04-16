import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# آدرس صفحه وب مورد نظر
url = 'https://arjang.ac.ir/calendar/full'

# دریافت محتوای صفحه وب
response = requests.get(url)
html_content = response.content

# تبدیل محتوا به یک شیء BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# پیدا کردن تمام عناصر دوره‌های آموزشی
courses = soup.find_all('div', class_='course')

# ساخت یک فایل Excel جدید
wb = Workbook()
ws = wb.active
ws.title = "Courses"

# افزودن عناوین ستون‌ها
ws.append(['عنوان', 'مدرس', 'هزینه'])

# گرفتن اطلاعات دوره‌ها و ذخیره در فایل Excel
for course in courses:
    title = course.find('h2').text.strip()
    instructor = course.find('p', class_='instructor').text.strip()
    price = course.find('p', class_='price').text.strip()
    ws.append([title, instructor, price])

# ذخیره فایل Excel
wb.save("arjang_courses.xlsx")
