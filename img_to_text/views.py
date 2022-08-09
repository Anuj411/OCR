from django.shortcuts import render
import pytesseract
from PIL import Image

def index(request):
    return render(request, 'index.html')

def postsubmit(request):
    file_image = request.FILES["img"]
    img = Image.open(file_image)

    pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'
    result = pytesseract.image_to_string(img)

    # with open('img_text.txt',mode ='w') as file:
    #     file.write(result)
    
    return render(request, 'index.html', {'text':result})