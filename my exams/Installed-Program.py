import subprocess
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def list_installed_programs():
    """
    Lists all installed programs on a Windows system.
    
    Returns:
    - list: A list of installed program names.
    """
    try:
        # Execute the wmic command to list installed programs
        result = subprocess.run(['wmic', 'product', 'get', 'name'], capture_output=True, text=True, check=True)
        
        # Extract installed program names from the command output
        installed_programs = result.stdout.strip().split('\n')[1:]
        
        return installed_programs
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return []

def create_pdf(programs, filepath):
    """
    Creates a PDF file containing the list of installed programs.
    
    Args:
    - programs (list): A list of installed program names.
    - filepath (str): The path of the PDF file to be created.
    """
    try:
        # Create a new PDF file
        c = canvas.Canvas(filepath, pagesize=letter)
        
        # Write the list of installed programs to the PDF file
        c.setFont("Helvetica", 12)
        c.drawString(100, 750, "List of Installed Programs:")
        y = 730
        for program in programs:
            c.drawString(100, y, program)
            y -= 20
        
        # Write the total number of installed programs to the PDF file
        c.drawString(100, y - 20, f"Total number of installed programs: {len(programs)}")
        
        # Save the PDF file
        c.save()
        
        print("PDF file created successfully.")
    except Exception as e:
        print("Error:", e)

# Get the current directory
current_directory = os.path.dirname(os.path.realpath(__file__))

# List installed programs
installed_programs = list_installed_programs()
if installed_programs:
    # Create PDF file in the current directory
    pdf_filepath = os.path.join(current_directory, "installed_programs.pdf")
    create_pdf(installed_programs, pdf_filepath)
else:
    print("No programs found.")
