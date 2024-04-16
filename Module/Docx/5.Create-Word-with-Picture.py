from docx import Document
from docx.shared import Inches

# ایجاد یک شیء Document جدید
doc = Document()

# افزودن تصویر با عنوان و اندازه مشخص
doc.add_picture('E:\\Project\\Python Project\\Module\\Docx\\hacker.jpg', width=Inches(2), height=Inches(2))

# ذخیره سند با نام مشخص
doc.save('document_with_image.docx')
