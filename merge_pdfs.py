import os
import random
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(paths, output_name, output_folder):
    """
    Merge multiple PDF files into a single file.
    
    :param paths: List of full paths to the PDF files.
    :param output_name: Name of the output PDF file.
    :param output_folder: Directory where the merged PDF will be saved.
    """
    # Create a PdfWriter object to write the combined PDF
    pdf_writer = PdfWriter()
    
    # Loop through all the provided PDF file paths
    for path in paths:
        pdf_reader = PdfReader(path)
        for page in pdf_reader.pages:
            # Add each page to the writer
            pdf_writer.add_page(page)
    
    # Save the combined PDF in the desired folder
    with open(os.path.join(output_folder, output_name), 'wb') as output_file:
        pdf_writer.write(output_file)

def find_pdfs(folder):
    """
    Find all PDF files in a folder and its subfolders.
    
    :param folder: Base directory to search for PDF files.
    :return: List of full paths to the found PDF files.
    """
    pdf_paths = []
    cover_path = None
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.pdf'):
                full_path = os.path.join(root, file)
                if file.lower() == 'portada.pdf':
                    cover_path = full_path
                else:
                    pdf_paths.append(full_path)
    if cover_path:
        pdf_paths.insert(0, cover_path)  # Insert cover at the start if it exists
    else:
        random.shuffle(pdf_paths)  # Shuffle paths if no cover is found
    return pdf_paths

# ===== Code Execution =====
base_folder = './output/modernidad'
output_folder = './output/modernidad'
output_name = 'modernidad-final.pdf'

# Find all PDFs in the base folder
pdf_paths = find_pdfs(base_folder)

# Merge the found PDFs
merge_pdfs(pdf_paths, output_name, output_folder)

print("PDFs successfully combined at:", os.path.join(output_folder, output_name))
