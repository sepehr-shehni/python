import os
from openpyxl import Workbook

# اجرای دستور arp -a و دریافت خروجی
output = os.popen('arp -a').read()

# جدا کردن خطوط از خروجی
lines = output.splitlines()

# ایجاد یک شیء Workbook جدید
wb = Workbook()
ws = wb.active

# افزودن داده‌ها به شیت
for line in lines:
    # جدا کردن اطلاعات هر خط
    parts = line.split()
    if len(parts) >= 2:
        ip_address = parts[0]
        mac_address = parts[1]
        ws.append([ip_address, mac_address])

# ذخیره فایل Excel
wb.save('arp_table.xlsx')
