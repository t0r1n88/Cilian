"""
Скрипт для отработки функционала который будет использоваться в графическом интерфейсе
"""
import pandas as pd
import openpyxl
import sys
import os,os.path
import shutil
from PyPDF2 import PdfMerger

path_folder_data = 'data'


for dirpath, dirnames, filenames in os.walk(path_folder_data):
    for filename in filenames:
        if filename.endswith('.rtf'):
            temp_str = dirpath.replace('/','\\')
            fio = temp_str.split('\\')[1]
            print(fio)
            name_test = temp_str.split('\\')[3]
            print(name_test)
            shutil.copyfile(f'{dirpath}/{filename}', f'temp/{fio}_{name_test}.rtf')

"""
Здесь работа Libre Office
"""

