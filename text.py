from PIL import Image
import pytesseract

# Set the tesseract_cmd to the path of tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image_path = 'textimg1.png'
image = Image.open(image_path)
extracted_text = pytesseract.image_to_string(image)
print(extracted_text)
