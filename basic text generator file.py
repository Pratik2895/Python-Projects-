import os,glob,fnmatch,tkinter

os.chdir(r"C:\Users\bhika\OneDrive\Desktop\moris lisa\dataentryproject")

from PIL import Image
import pytesseract
import cv2
import cv
import glob

from pytesseract import image_to_string 
from PIL import Image

#img=cv2.imread(r"C:\Users\bhika\OneDrive\Desktop\moris lisa\dataentryproject\1.jpg")
pytesseract.pytesseract.tesseract_cmd =r"C:\Program Files\Tesseract-OCR\tesseract.exe"

list=['C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\1.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\10.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\100.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\101.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\102.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\11.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\12.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\13.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\14.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\15.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\16.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\17.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\18.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\19.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\2.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\20.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\21.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\22.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\23.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\24.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\25.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\26.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\27.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\28.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\29.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\3.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\30.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\31.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\32.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\33.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\34.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\35.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\36.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\37.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\38.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\39.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\4.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\40.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\41.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\42.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\43.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\44.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\45.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\46.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\47.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\48.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\49.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\5.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\50.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\51.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\52.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\53.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\54.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\55.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\56.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\57.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\58.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\59.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\6.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\60.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\61.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\62.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\63.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\64.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\65.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\66.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\67.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\68.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\69.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\7.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\70.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\71.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\72.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\73.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\74.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\75.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\76.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\77.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\78.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\79.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\8.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\80.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\81.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\82.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\83.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\84.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\85.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\86.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\87.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\88.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\89.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\9.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\90.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\91.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\92.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\93.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\94.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\95.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\96.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\97.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\98.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\99.jpg', 'C:\\Users\\bhika\\OneDrive\\Desktop\\moris lisa\\dataentryproject\\file1.txt']
for file in list:
    print(pytesseract.image_to_string(Image.open(file),lang='eng'))
    text =  pytesseract.image_to_string(Image.open(file),lang='eng')
    with open(f"{file}.txt", mode = 'w') as f:
        f.write(text)
