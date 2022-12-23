import os,os.path
import shutil
from PyPDF2 import PdfMerger


file_dct = dict()
#
for file in os.listdir('out'):
    temp_lst = file.split('.')[0].split('_')
    if temp_lst[0] not in file_dct:
        file_dct[temp_lst[0]] = []
    else:
        file_dct[temp_lst[0]].append(file)
#
#
for lst_pdf in file_dct.values():
    merger = PdfMerger()
    for pdf in lst_pdf:
        merger.append(f'out/{pdf}')
    merger.write(f'{"itog"}/{lst_pdf[0].split("_")[0]}.pdf')
#     merger.close()