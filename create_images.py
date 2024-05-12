import os
from PIL import Image, ImageDraw, ImageFont

def load_background_image(path):
    """Carga una imagen de fondo desde un archivo."""
    try:
        return Image.open(path)
    except IOError:
        print("No se pudo cargar la imagen de fondo.")
        return None

def wrap_text(text, font, max_width):
    """Divide el texto en líneas que no superen el ancho máximo, respetando los saltos de línea explícitos."""
    wrapped_lines = []
    paragraphs = text.split('\n')
    for paragraph in paragraphs:
        if paragraph:
            words = paragraph.split()
            current_line = ''
            for word in words:
                test_line = f'{current_line} {word}' if current_line else word
                if font.getsize(test_line)[0] <= max_width:
                    current_line = test_line
                else:
                    wrapped_lines.append(current_line)
                    current_line = word
            wrapped_lines.append(current_line)
        wrapped_lines.append('')
    return wrapped_lines

def create_images_with_text(background_path, text_path, font_path, font_size=20, writting_path='default'):
    """Crea múltiples imágenes con texto sobre un fondo específico."""
    background_image = load_background_image(background_path)
    if not background_image:
        return None

    with open(text_path, 'r', encoding='utf-8') as file:
        text = file.read()

    font = ImageFont.truetype(font_path, font_size)
    # adjust lateral margin to 40px each side
    max_width = background_image.width - 80 
    wrapped_lines = wrap_text(text, font, max_width)

    # adjust vertical margin to 5px each side
    max_height = background_image.height - 10
    line_height = font.getsize('Wg')[1]
    lines_per_image = (max_height // line_height) + 5

    output_folder = os.path.join('output', writting_path)
    # remove previous images
    for file in os.listdir(output_folder):
        os.remove(os.path.join(output_folder, file))
    os.makedirs(output_folder, exist_ok=True)

    images = []
    for start in range(0, len(wrapped_lines), lines_per_image):
        img = background_image.copy()
        draw = ImageDraw.Draw(img)
        # set initial vertical margin to 25px
        y_position = 25
        for line in wrapped_lines[start:start + lines_per_image]:
            # 40 is the left margin
            draw.text((40, y_position), line, font=font, fill="black")
            y_position += line_height if line else (line_height / 3)
        image_path = os.path.join(output_folder, f"{writting_path}_{len(images) + 1}.jpg")
        img.save(image_path)
        images.append(img)

    return images


# routes and configurations
assets_path = './assets/'
background_path = f"{assets_path}background.jpg"
text_path = "./contenido.txt"
font_path = f"{assets_path}font.ttf"
writting_path = "modernidad"

# main execution
if __name__ == "__main__":
    images = create_images_with_text(background_path, text_path, font_path, 20, writting_path)
