##Import Extraction Libraries
import docx2txt
from pdfminer.high_level import extract_text

import aspose.words as aw
#Functions for conversion
def convertPDFToText(file_path):
    return extract_text(file_path)
    

def convertDocxToText(file_path):
    return docx2txt.process(file_path)