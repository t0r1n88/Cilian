"""
Скрипт для отработки функционала который будет использоваться в графическом интерфейсе
"""
import pandas as pd
import openpyxl
import sys
import os,os.path
import shutil
from PyPDF2 import PdfMerger

path_folder_data = 'data/'


for dirpath, dirnames, filenames in os.walk(path_folder_data):
                    for filename in filenames:
                        if filename.endswith('.rtf'):
                            temp_str = dirpath.replace('/','\\')
                            fio = temp_str.split('\\')[1]
                            print(fio)
                            name_test = temp_str.split('\\')[3]
                            print(name_test)
                            shutil.copyfile(f'{dirpath}/{filename}', f'temp/{fio}_{name_test}.rtf')

file_dct = dict()

for file in os.listdir('out'):
    temp_lst = file.split('.')[0].split('_')
    if temp_lst[0] not in file_dct:
        file_dct[temp_lst[0]] = []
    else:
        file_dct[temp_lst[0]].append(file)


for lst_pdf in file_dct.values():
    merger = PdfMerger()
    for pdf in lst_pdf:
        merger.append(f'out/{pdf}')
    merger.write(f'{lst_pdf[0].split("_")[0]}.pdf')
    merger.close()