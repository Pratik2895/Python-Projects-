import re
from pdf2image import convert_from_path
from PIL import Image
import numpy as np
import cv2
import  pytesseract
import utillity

poplerpath=r"C:\Release-23.07.0-0\poppler-23.07.0\Library\bin" 
file_path=r"docs\prescription\pre_1.pdf"
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'






def extract(file_path,file_format):
    pages = convert_from_path(file_path,poppler_path=poplerpath)
    document_text=""
    for page in pages:
        processed_image=utillity.preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang='eng')
        document_text=text+"\n"
    return document_text


    # if file_format == 'prescriptions':
    #     pass
    # elif file_format == 'patient_details':
    #     pass





    
    
if __name__ == "__main__":
    data=extract(r"resources\patient_details\pd_2.pdf",'prescriptions')
    print(data)