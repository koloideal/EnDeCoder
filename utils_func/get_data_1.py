import os
import helper


def get_data_1():

    while True:

        print('\nВыбери способ шифровки/дешифровки текста(Введи цифру)')

        for k, i in helper.name_func.items():

            print(f'{k}. {i}')

        encryption_method = input()

        if encryption_method not in ['1', '2', '3', '4', '5', '6']:

            continue

        else:

            break

    while True:

        encoding_or_decoding = input('\nНеобходимо шифровать или расшифровать текст?(Введи цифру)\n'
                                     '1. Шифровать\n'
                                     '2. Расшифровать\n')

        if encoding_or_decoding not in ['1', '2']:

            continue

        else:

            break

    while True:

        file_name = input("\nВведи название файла без расширения: ")

        if os.path.isfile(f'content/{file_name}.txt'):

            with open(f'content/{file_name}.txt', 'r', encoding='utf8') as file:

                content = file.read().split('\n')

            break

        else:

            print('Файл не найден')

    match encoding_or_decoding:

        case '1':

            helper.name_func_to_func[int(encryption_method)][0](content, file_name)

        case '2':

            helper.name_func_to_func[int(encryption_method)][1](content, file_name)
