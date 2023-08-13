from pdf2image import convert_from_path, convert_from_bytes
# from IPython.display import display, Image
# from google.colab import drive
# from PyPDF2 import PdfReader
import pytesseract
import glob
import PIL
PIL.Image.MAX_IMAGE_PIXELS = 933120000
# pdfs = glob.glob(r"content2.pdf")

pdfs = open("*.pdf", "r")

def ocr_pdf(pdf)
    pdf_text = ""
    for pdf_path in pdfs:
        pages = convert_from_path(pdf_path, 1500)
        print(pdf_path,"to text below:\n\n")
        for pageNum,imgBlob in enumerate(pages):
            text = pytesseract.image_to_string(imgBlob,lang='eng')

print(pdf_text,pdfs)