from user_encryption.user_encryption import encode_user_encryption, decode_user_encryption
import os


def helper_encode_config_input(data: dict) -> None:

    match data["where_get_data"]:

        case "file":

            while True:

                file_name = input("\nВведи название файла без расширения: ")

                if os.path.isfile(f'content/{file_name}.txt'):

                    with open(f'content/{file_name}.txt', 'r', encoding='utf8') as file:

                        content = file.read().split('\n')

                    encryption_symbols = {}

                    for i in data["encryption_symbols"].split(','):

                        encryption_symbols[i.replace(' ', '')[0]] = i.replace(' ', '')[2]

                    with open(f'content/{file_name}(encoded).txt', 'w', encoding='utf8') as file:

                        for line in content:

                            file.write(encode_user_encryption(encryption_symbols, line, data["escape_symbol"]) + '\n')

                    print(f'\nФайл {file_name}(encoded).txt успешно создан')

                    return

                else:

                    print('Файл не найден')

                    continue

        case "manual":

            encryption_symbols = {}

            for i in data["encryption_symbols"].split(','):

                encryption_symbols[i.replace(' ', '')[0]] = i.replace(' ', '')[2]

            string = input("\nВведите строку: ")

            print(encode_user_encryption(encryption_symbols, string, data["escape_symbol"]))

            return


def helper_decode_config_input(data: dict) -> None:

    match data["where_get_data"]:

        case "file":

            while True:

                file_name = input("\nВведи название файла без расширения: ")

                if os.path.isfile(f'content/{file_name}.txt'):

                    with open(f'content/{file_name}.txt', 'r', encoding='utf8') as file:

                        content = file.read().split('\n')

                    encryption_symbols = {}

                    for i in data["encryption_symbols"].split(','):

                        encryption_symbols[i.replace(' ', '')[0]] = i.replace(' ', '')[2]

                    with open(f'content/{file_name}(decoded).txt', 'w', encoding='utf8') as file:

                        for line in content:

                            file.write(decode_user_encryption(encryption_symbols, line, data["escape_symbol"]) + '\n')

                    print(f'\nФайл {file_name}(decoded).txt успешно создан')

                    return

                else:

                    print('Файл не найден')

                    continue

        case "manual":

            encryption_symbols = {}

            for i in data["encryption_symbols"].split(','):

                encryption_symbols[i.replace(' ', '')[0]] = i.replace(' ', '')[2]

            string = input("\nВведите строку: ")

            print(decode_user_encryption(encryption_symbols, string, data["escape_symbol"]))

            return
