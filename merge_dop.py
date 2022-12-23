import os,os.path
import shutil
from PyPDF2 import PdfMerger


file_dct = dict()
#
for file in os.listdir('out'):
    temp_lst = file.split('.')[0].split('_')
    if temp_lst[1] not in file_dct:
        file_dct[temp_lst[1]] = []
    else:
        file_dct[temp_lst[1]].append(file)

# print(file_dct)
for lst_pdf in file_dct.values():
    print(lst_pdf)
    merger = PdfMerger()
    for pdf in lst_pdf:
        merger.append(f'out/{pdf}')

    # print(lst_pdf)
    # print(lst_pdf[0].split('_')[1])
    # merger.write(f'{"itog"}/{lst_pdf[0].split("_")[0]}.pdf')
    print(lst_pdf[0].split("_")[1])
    merger.write(f'{"itog"}/{lst_pdf[0].split("_")[1]}.pdf')