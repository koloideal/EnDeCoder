import os
import helper


def get_data_file() -> None:

    while True:

        print('\nChoose a way to encrypt/decrypt the text (Enter a number)')

        for k, i in helper.name_func.items():

            print(f'{k}. {i}')

        encryption_method: str = input()

        if encryption_method not in ['1', '2', '3', '4', '5', '6']:

            continue

        else:

            break

    while True:

        encoding_or_decoding: str = input('\nDo I need to encrypt or decrypt the text?(Enter a number)\n'
                                          '1. Encode\n'
                                          '2. Decode\n')

        if encoding_or_decoding not in ['1', '2']:

            continue

        else:

            break

    while True:

        file_name: str = input('\nEnter the name of the file without the extension: ')

        if os.path.isfile(f'content/{file_name}.txt'):

            with open(f'content/{file_name}.txt', 'r', encoding='utf8') as file:

                content: list = file.read().split('\n')

            break

        else:

            print('File was not found')

    match encoding_or_decoding:

        case '1':

            helper.name_func_to_func[int(encryption_method)][0](content, file_name)

        case '2':

            helper.name_func_to_func[int(encryption_method)][1](content, file_name)
