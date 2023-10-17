
# #PyPDF2
# #Extracts text well with correct spacing inbetween (new line) but has problems with the left to right allignments causing certain spaces in words
# #unable to extract text from word document (docx. file)

# # importing required modules 
# from PyPDF2 import PdfReader 
  
# # creating a pdf reader object 
# reader = PdfReader('Charlotte Clerx CV.pdf') 
# #reader = PdfReader('Resume-HDB.docx')  
# # printing number of pages in pdf file 
# print(len(reader.pages)) 
  
# # getting a specific page from the pdf file 
# page = reader.pages[0] 
  
# # extracting text from page 
# text = page.extract_text() 
# print(text) 



# Textract
# For the default textextract instead of spaces it doesnt show space instead it shows it as /n and /r etc.
# When attempting to incorporate the pdf miner engine into the textract, it was unable to do so due to presence of a NoneType
# able to extract all special symbol except ' and "

# import textract
# text = textract.process('Charlotte Clerx CV.pdf')
# #text = textract.process('Resume-HDB.docx')
# #text = textract.process('RayResume.docx')
# #text = textract.process('Charlotte Clerx CV.pdf', method='pdfminer')
# print(text)



#PyMuPDF

# import fitz
# doc = fitz.open("Lu__Zhang_-_L & D Business Developer_230724_203254 (1).pdf")
# #doc = fitz.open('Resume-HDB.docx')
# for page in doc: 
#   text = page.get_text() 
#   print(text)

# #extract image from pdf
# for page in doc: 
#     pix = page.get_pixmap(matrix=fitz.Identity, dpi=None, 
#                           colorspace=fitz.csRGB, clip=None, alpha=True, annots=True) 
#     pix.save("samplepdfimage-%i.png" % page.number)  # save file 

# #image to text
# from PIL import Image
# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Shaun Ho\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
# print(pytesseract.image_to_string(Image.open('testingimg.png')))



