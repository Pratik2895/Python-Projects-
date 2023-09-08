from parser_generic_practice import MedicalDocParser
import abc
import re


class PrescriptionParser (MedicalDocParser):
    def __init__ (self,text):
        MedicalDocParser.__init__(self,text)

    def parse(self):
        pass

    def get_name(self):
        pattern = 'Name:(.*)Date'
        matches = re.findall(pattern, self.text)
        if len(matches)>0:
            repr = matches[0].strip()


if __name__ == "__main__":
     document_text = '''
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222
Name: Marta Sharapova Date: 5/11/2022
Address: 9 tennis court, new Russia, DC

Prednisone 20 mg
Lialda 2.4 gram
Directions:
Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks -
Lialda - take 2 pill everyday for 1 month
Refill: 3 times
'''
    
pp=PrescriptionParser(document_text)
pp.get_name()

          
 