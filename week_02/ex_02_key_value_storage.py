#https://www.coursera.org/learn/diving-in-python/programming/nc6Ce/key-value-khranilishchie
'''подключаем модули

определяется путь хранения файла json и переменная хранения

парсятся значения, введенные в коммандной строке, определяется key и val

если переданы значения key и val, то:
    прочитать файл
    прочитанное значение поместить в переменную хранения
    проверить наличие ключа в хранилище, если ключ есть, то:
        добавляем val в список данных по ключу
    иначе:
        создать ключ, в список положить val
    записать файл

если передано только значение key, то:
    прочитать файл
    прочитанное значение поместить в переменную хранения
    проверить наличие ключа в хранилище, если ключ есть, то:
        отображаем данные ключа
    иначе:
        выводим сообщение об отсутствии ключа
    записать файл'''

#$ storage.py --key key_name --val value
#$ storage.py --key key_name



#подключаем модули
import argparse
import json
import os
import tempfile

def args():
    #парсятся значения, введенные в коммандной строке,
    #определяется key и val
    parser = argparse.ArgumentParser()
    parser.add_argument('--key')
    parser.add_argument('--val')
    #получаем кортеж с key и val 
    return parser.parse_args()
    
def read_data(storage_path):
    #читаем данные из файла
    with open(storage_path, 'r') as f:
        #не определено действие в случае попытки 
        #чтения из пустого файла. Отдаю пустой словарь,
        #если файл пуст
        if os.path.getsize (storage_path):
            return json.load(f)
        else:
            return {}
        
def write_data(storage_path, data):
    #записать файл
    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))
    
        
#----------------------------------------------------------

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
data = {}
args = args()
#print('key = {}, val = {}'.format(args.key, args.val))

#если переданы оба значения (key и val)
if args.key and args.val:
    data = read_data(storage_path)
    #если ключа нет
    if args.key not in data:
        #создать ключ
        data[args.key] = list()
    #в список положить val
    data[args.key].append(args.val)
    write_data(storage_path, data)
#если передано только key и не передано val
elif args.key and not args.val:
    data = read_data(storage_path)
    #если ключа нет
    if args.key not in data:
        #выводим None или  пустую строку
        print('None')
    else:
        #отображаем данные ключа
        print(str(data[args.key]).replace("'", '').replace("]", '').replace("[", ''))