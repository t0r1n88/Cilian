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
    # Получаем ФИО
    fio = filename_master.split('_')[0]
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
    composer.save(f"{path_end_folder}/{fio}.docx")


path_end_folder = 'ITOG'
path_folder_data = 'IN'
path_docx_data = 'DOCX'
path_rtf = 'RTF'

# Извлекаем RTF в папку RTF

for dirpath, dirnames, filenames in os.walk(path_folder_data):
    for filename in filenames:
        if filename.endswith('.rtf'):
            temp_str = dirpath.replace('/','\\')
            fio = temp_str.split('\\')[1]
            name_test = temp_str.split('\\')[3]
            shutil.copyfile(f'{dirpath}/{filename}', f'{path_rtf}/{fio}_{name_test}.rtf')

"""
Здесь работа Libre Office
"""
# Объединение
#Создаем словарь для каждого школьника
# file_dct = dict()
# #
# for file in os.listdir('DOCX'):
#     temp_lst = file.split('.')[0].split('_')
#     if temp_lst[0] not in file_dct:
#         file_dct[temp_lst[0]] = []
#     else:
#         file_dct[temp_lst[0]].append(file)
#
# for lst_docx in file_dct.values():
#     combine_all_docx(lst_docx[0],lst_docx[1:])

