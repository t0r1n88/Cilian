"""
Скрипт для отработки функционала который будет использоваться в графическом интерфейсе
"""
import pandas as pd
import openpyxl
import sys
import os,os.path
import shutil
from PyPDF2 import PdfMerger
from docxtpl import DocxTemplate
from docxcompose.composer import Composer
from docx import Document
import time

def combine_all_docx(filename_master, files_lst):
    """
    Функция для объединения файлов Word взято отсюда
    https://stackoverflow.com/questions/24872527/combine-word-document-using-python-docx
    :param filename_master: базовый файл
    :param files_list: список с созданными файлами
    :return: итоговый файл
    """

    # Получаем текущее время
    t = time.localtime()
    current_time = time.strftime('%H_%M_%S', t)

    number_of_sections = len(files_lst)
    # Открываем и обрабатываем базовый файл
    master = Document(f'{path_docx_data}/{filename_master}')
    composer = Composer(master)
    # Перебираем и добавляем файлы к базовому
    for i in range(0, number_of_sections):
        doc_temp = Document(f'{path_docx_data}/{files_lst[i]}')
        composer.append(doc_temp)
    # Сохраняем файл
    composer.save(f"{path_end_folder}/Общий файл  от {current_time}.docx")

path_folder_data = 'group_result'
path_end_folder = 'ITOG_group'
path_docx_data = 'DOCX_group'
path_rtf = 'RTF_group'
# Извлекаем RTF в папку RTF
for dirpath, dirnames, filenames in os.walk(path_folder_data):
    for filename in filenames:
        if filename.endswith('.rtf'):
            temp_str = dirpath.replace('/','\\')
            name_test  = temp_str.split('\\')[1]
            shutil.copyfile(f'{dirpath}/{filename}', f'{path_rtf}/{name_test}.rtf')


"""
Здесь работа Libre Office
"""


combine_all_docx(os.listdir(path_docx_data)[0],os.listdir(path_docx_data)[1:])

# for lst_docx in file_dct.values():
#     combine_all_docx(lst_docx[0],lst_docx[1:])

