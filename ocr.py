from PIL import Image
import pytesseract

# Open the image
image = Image.open("sample.png")

# Extract text
text = pytesseract.image_to_string(image)

print(text)  # Output extracted text
