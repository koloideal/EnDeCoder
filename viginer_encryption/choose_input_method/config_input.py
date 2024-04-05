from viginer_encryption.viginer_encryption import encode_viginer_encryption, decode_viginer_encryption
import os


def helper_encode_config_input(data: dict) -> None:

    match data['where_get_data']:

        case 'file':

            while True:

                file_name: str = input('\nEnter the name of the file without the extension: ')

                if os.path.isfile(f'content/{file_name}.txt'):

                    with open(f'content/{file_name}.txt', 'r', encoding='utf8') as file:

                        content: list = file.read().split('\n')

                    list_with_len_lines: list = [len(line) for line in content]

                    encoded_string: str = encode_viginer_encryption(''.join(content), data["key_word"], data["save_register"])

                    result_list: list = []

                    long: int = 0

                    for line in list_with_len_lines:

                        result_list.append(encoded_string[long:line + long])

                        long += line

                    with open(f'content/{file_name}(encoded).txt', 'w', encoding='utf8') as file:

                        for line in result_list:

                            file.write(line + '\n')

                    print(f'\nFile "{file_name}(encoded).txt" successfully created')

                    break

                else:

                    print('File was not found')

                    continue

        case 'manual':

            string: str = input('\nEnter the text: ')

            print(encode_viginer_encryption(string, data['key_word'], data['save_register']))

            return


def helper_decode_config_input(data: dict) -> None:

    match data['where_get_data']:

        case 'file':

            while True:

                file_name: str = input('\nEnter the name of the file without the extension: ')

                if os.path.isfile(f'content/{file_name}.txt'):

                    with open(f'content/{file_name}.txt', 'r', encoding='utf8') as file:

                        content: list = file.read().split('\n')

                    list_with_len_lines: list = [len(line) for line in content]

                    encoded_string: str = decode_viginer_encryption(''.join(content), data['key_word'], data['save_register'])

                    result_list: list = []

                    long: int = 0

                    for line in list_with_len_lines:

                        result_list.append(encoded_string[long:line + long])

                        long += line

                    with open(f'content/{file_name}(decoded).txt', 'w', encoding='utf8') as file:

                        for line in result_list:

                            file.write(line + '\n')

                    print(f'\nFile "{file_name}(decoded).txt" successfully created')

                    break

                else:

                    print('File was not found')

                    continue

        case 'manual':

            string: str = input('\nEnter the text: ')

            print(decode_viginer_encryption(string, data['key_word'], data['save_register']))

            return
