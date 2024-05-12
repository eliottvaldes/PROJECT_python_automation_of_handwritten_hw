from fpdf import FPDF
import datetime
import locale

# Set the locale for datetime formatting
locale.setlocale(locale.LC_TIME, 'es_MX.UTF-8')

def create_pdf(cover_path, pdf_path, content_info):
    try:
        pdf = FPDF()
        pdf.add_page()
        add_image(pdf, cover_path)  # Use the cover_path argument
        add_personal_info(pdf, content_info)
        pdf.output(pdf_path)  # Use the pdf_path argument
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print(f"PDF file successfully created at {pdf_path}")

def add_image(pdf, image_path):
    """Adds an image covering the top 50% of the page."""
    width, height = 210, 297  # A4 paper dimensions in mm
    pdf.image(image_path, x=0, y=0, w=width, h=height/2)

def add_personal_info(pdf, content_info):
    """Adds personal information in the middle and end of the page."""
    # Set text properties for 'writing_path'
    pdf.set_text_color(150, 100, 225)  # A purplish blue color
    pdf.set_font('Arial', '', 26)
    pdf.set_y(180)  # Set y position after image
    pdf.cell(0, 10, content_info['writing_path'], align='C', ln=True)
    
    # Reset text color to black for remaining information
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Arial', 'B', 18)
    pdf.cell(0, 10, content_info['name'], align='C', ln=True)
    
    pdf.set_font('Arial', 'I', 14)
    pdf.cell(0, 10, f"Fecha: {content_info['current_date']}", align='C', ln=True)
    pdf.cell(0, 10, f"Grupo: {content_info['student_group']}", align='C', ln=True)
    pdf.cell(0, 10, f"Materia: {content_info['student_subject']}", align='C', ln=True)




# ============ execution
# Define content information and file paths
content_info = {
    'writing_path': 'Titulo de Actividad',
    'name': 'Eliot Fabián Valdés Luis',
    'current_date': datetime.datetime.now().strftime('%d de %B de %Y'),
    'student_group': '5VB1',
    'student_subject': 'Aprendizaje Máquina'
}
cover_path = './assets/cover.jpg'
pdf_path = './output/Portada.pdf'

# Execute the program
create_pdf(cover_path, pdf_path, content_info)
