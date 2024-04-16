from docx import Document

# ایجاد یک شیء Document جدید
doc = Document()

# ایجاد یک پاراگراف جدید و اضافه کردن متن به آن
paragraph = doc.add_paragraph('This is a paragraph.')

# ذخیره سند با نام مشخص
doc.save('document_with_paragraph.docx')
