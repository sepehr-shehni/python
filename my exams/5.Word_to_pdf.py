from docx import Document
from docx.shared import Inches
from docx2pdf import convert

def create_word_file(text, filename):
    """
    Create a Word file with the given text.
    
    Args:
    - text (str): The text to write into the Word file.
    - filename (str): The name of the Word file to create.
    """
    document = Document()
    document.add_paragraph(text)
    document.save(filename)
    print(f"Word file '{filename}' created successfully.")

def convert_to_pdf(filename):
    """
    Convert a Word file to PDF.
    
    Args:
    - filename (str): The name of the Word file to convert.
    """
    pdf_filename = filename.split('.')[0] + '.pdf'
    convert(filename, pdf_filename)
    print(f"Word file '{filename}' converted to PDF '{pdf_filename}'.")

# Get input text from user
text = input("Enter the text: ")

# Define the filename for Word file
word_filename = "output.docx"

# Create a Word file with the input text
create_word_file(text, word_filename)

# Convert the Word file to PDF
convert_to_pdf(word_filename)
