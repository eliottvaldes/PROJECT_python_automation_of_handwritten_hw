import os
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def get_image_paths(output_folder, writting_path):
    """Obtiene todas las rutas de las imágenes en la carpeta especificada, ordenadas alfabéticamente."""
    path = os.path.join(output_folder, writting_path)
    image_files = [os.path.join(path, f) for f in sorted(os.listdir(path), key=lambda x: int(x.split('_')[-1].split('.')[0])) if f.endswith('.jpg')]
    return image_files

def create_pdf_from_images(image_paths, writting_path):
    """Crea un PDF a partir de las imágenes proporcionadas."""
    if not image_paths:
        print("No hay imágenes para incluir en el PDF.")
        return

    pdf_path = os.path.join('PDF', f'{writting_path}.pdf')
    os.makedirs('PDF', exist_ok=True)
    
    c = canvas.Canvas(pdf_path, pagesize=letter)
    # get dimensions of letter size
    width, height = letter  

    for image_path in image_paths:
        im = Image.open(image_path)
        im_width, im_height = im.size
        ratio = min(width / im_width, height / im_height)
        im = im.resize((int(im_width * ratio), int(im_height * ratio)), Image.ANTIALIAS)

        # Center the image
        c.drawInlineImage(im, x=(width - im_width * ratio) / 2, y=(height - im_height * ratio) / 2, width=im_width * ratio, height=im_height * ratio)
        c.showPage()

    c.save()
    print(f"PDF creado exitosamente en {pdf_path}")

# code execution
if __name__ == "__main__":
    # define the folder where the images are stored and the name of the folder and the pdf
    writting_path = "modernidad" 
    output_folder = 'output'
    image_paths = get_image_paths(output_folder, writting_path)
    create_pdf_from_images(image_paths, writting_path)
