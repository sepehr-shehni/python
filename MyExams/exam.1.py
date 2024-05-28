import os
import requests
from bs4 import BeautifulSoup
from fpdf import FPDF

# تابعی برای دریافت و پارس کردن HTML صفحه وب
def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch page: {url}, Status code: {response.status_code}")

# تابعی برای استخراج لیست اساتید
def scrape_professors(html):
    soup = BeautifulSoup(html, 'html.parser')
    professors = []

    # یافتن تمامی تگ‌های <a> که حاوی نام اساتید هستند
    for a_tag in soup.find_all('a'):
        name = a_tag.text.strip()
        professors.append(name)

    return professors

# تابعی برای ذخیره لیست اساتید در یک فایل PDF
def save_to_pdf(professors, filename):
    pdf = FPDF()
    pdf.add_page()
    
    # استفاده از فونت Unicode با نام font.ttf که در همان پوشه کد قرار دارد
    font_path = 'E:\\python project\\MyExams\\Vazirmatn-Regular.ttf'
    pdf.add_font('vazir', '', font_path, uni=True)
    pdf.set_font('vazir', '', 12)

    for professor in professors:
        pdf.cell(200, 10, txt=professor, ln=True)

    pdf.output(filename)

# تابع اصلی
def main():
    url = 'https://arjang.ac.ir//instructors/'  # آدرس URL مورد نظر
    html = fetch_html(url)
    professors = scrape_professors(html)

    if professors:
        # یافتن مسیر دسکتاپ
        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        pdf_path = os.path.join(desktop_path, 'professors_list.pdf')
        
        save_to_pdf(professors, pdf_path)
        print('PDF created successfully on Desktop.')
    else:
        print('No professors found.')

if __name__ == '__main__':
    main()
