from docx import Document

# ایجاد یک شیء Document جدید با عنوان مشخص
doc = Document()
doc.add_heading('My Document Title', level=1)

# ذخیره سند با نام مشخص
doc.save('document_with_title.docx')
