from pdf2docx import Converter
import os

path_input = 'ruta_archivo_pdf'
path_output = 'ruta_para_el_archivo_word_generado'

for file in os.listdir(path_input):
    cv = Converter(path_input+file)
    cv.convert(path_output+file+'.docx', start=0, end=None)
    cv.close()
    print(file)