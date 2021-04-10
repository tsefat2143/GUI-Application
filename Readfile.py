import docx
import os

os.getcwd()

doc = docx.Document('template.docx')
print(doc.paragraphs)
