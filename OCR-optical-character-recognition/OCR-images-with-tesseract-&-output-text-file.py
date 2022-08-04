# download and install Tesseract in your machine for your specific operating system (https://tesseract-ocr.github.io/tessdoc/Installation.html)
# install Pytesseract with pip using cmd ("pip install pytesseract")

from PIL import Image
import pytesseract

# To use Tesseract, in the Python code you must specify the path of tesseract.exe (or insert it in the system environment variables: https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/)
## that in the default installation options is normally saved in C:/Users/AppData/Local/Tesseract-OCR/tesseract.exe

pytesseract.pytesseract.tesseract_cmd = ''  #insert the path of tesseract.exe in the quotes

# Here are three ways to customize the settings (engine modes, page segmentation modes or boths)
custom_oem_config = r'--oem 3'
custom_psm_config = r'--psm 3'
custom_oem_psm_config = r'--oem 3 --psm 3'


# path of the file image you want to OCR
file = ""

#we open and then we OCR the file (we can specify language and settings)
with open(file, 'rb') as inputFile:
    img = Image.open(inputFile)
    ocrText = pytesseract.image_to_string(img, lang="ita", config=custom_oem_psm_config)

#we retrieve the name the name for the output file
fileName = file.rsplit('/')[-1]
fileName = fileName.rsplit('.')[0]

#we create the news file with the OCR'ed text
folder = ""  #insert in the quites the folder in which you want store the new text file
with open(folder + fileName + ".txt", "w", encoding="utf-8") as outFile:
    outFile.write(ocrText)

print(fileName, "text file successfully created.")
