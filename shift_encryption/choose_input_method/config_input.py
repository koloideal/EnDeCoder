from shift_encryption.shift_encryption import encode_shift_encryption, decode_shift_encryption
import os


def helper_encode_config_input(data: dict) -> None:

    match data['where_get_data']:

        case 'file':

            while True:

                file_name: str = input('\nEnter the name of the file without the extension: ')

                if os.path.isfile(f'content/{file_name}.txt'):

                    with open(f'content/{file_name}.txt', 'r', encoding='utf8') as file:

                        content: list = file.read().split('\n')

                    with open(f'content/{file_name}(encoded).txt', 'w', encoding='utf8') as file:

                        for line in content:

                            file.write((encode_shift_encryption(data['shift'], line, data['save_register']) + '\n'))

                    print(f'\nFile "{file_name}(encoded).txt" successfully created')

                    return

                else:

                    print('File was not found')

                    continue

        case 'manual':

            string: str = input('\nEnter the text: ')

            print(encode_shift_encryption(data['shift'], string, data['save_register']))

            return


def helper_decode_config_input(data: dict) -> None:

    match data['where_get_data']:

        case 'file':

            while True:

                file_name: str = input('\nEnter the name of the file without the extension: ')

                if os.path.isfile(f'content/{file_name}.txt'):

                    with open(f'content/{file_name}.txt', 'r', encoding='utf8') as file:

                        content: list = file.read().split('\n')

                    with open(f'content/{file_name}(decoded).txt', 'w', encoding='utf8') as file:

                        for line in content:

                            file.write((decode_shift_encryption(data['shift'], line, data['save_register']) + '\n'))

                    print(f'\nFile "{file_name}(decoded).txt" successfully created')

                    return

                else:

                    print('File was not found')

                    continue

        case 'manual':

            string: str = input('\nEnter the text: ')

            print(decode_shift_encryption(data['shift'], string, data['save_register']))

            return
