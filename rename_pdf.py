import os,os.path
import shutil
import pandas as pd
import random

lst_miss = []  # создаем список в котором будем хранить названия готовых файлов

for file in os.listdir('itog'):  # заполняем список
    lst_miss.append(file)

len_lst_miss = len(lst_miss)  # получаем длину списка

for file in os.listdir('Списки'):
    file_name = file.split('.')[0]
    df = pd.read_excel(f'Списки/{file}')
    lst_fio = df['ФИО'].tolist()

    for fio in lst_fio:
        rand_index = random.randint(0,len_lst_miss-1) # получаем рандомный индекс
        if os.path.exists(f'miss_fio/{file_name}'):
            shutil.copyfile(f'{"itog"}/{lst_miss[rand_index]}', f'miss_fio/{file_name}/{fio}.pdf')
        else:
            os.mkdir(f'miss_fio/{file_name}')
            shutil.copyfile(f'{"itog"}/{lst_miss[rand_index]}', f'miss_fio/{file_name}/{fio}.pdf')

