import pyttsx3
import uuid
from numpy import extract
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

def pdf_to_string(file_path):
    output_string = StringIO()
    with open(file_path, 'rb') as file:
        parser = PDFParser(file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
        return(output_string.getvalue())

def string_to_audio(engine, string, filetype):
    filename = str(uuid.uuid4().hex) + filetype
    engine.save_to_file( string, "C:/Users/Josmelvy/Desktop/" +filename)
    engine.runAndWait()
    engine.stop()   

