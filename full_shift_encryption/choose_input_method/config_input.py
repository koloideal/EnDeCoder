from full_shift_encryption.full_shift_encryption import encode_full_shift_encryption, decode_full_shift_encryption
import os


def helper_encode_config_input(data: dict) -> None:

    match data["where_get_data"]:

        case "file":

            while True:

                file_name = input("\nВведи название файла без расширения: ")

                if os.path.isfile(f'content/{file_name}.txt'):

                    with open(f'content/{file_name}.txt', 'r', encoding='utf8') as file:

                        content = file.read().split('\n')

                    with open(f'content/{file_name}(encoded).txt', 'w', encoding='utf8') as file:

                        for line in content:

                            file.write((encode_full_shift_encryption(data["shift"], line)) + '\n')

                    print(f'\nФайл {file_name}(encoded).txt успешно создан')

                    return

                else:

                    print('Файл не найден')

                    continue

        case "manual":

            string = input("\nВведите строку: ")

            print(encode_full_shift_encryption(data["shift"], string))

            return


def helper_decode_config_input(data: dict) -> None:

    match data["where_get_data"]:

        case "file":

            while True:

                file_name = input("\nВведи название файла без расширения: ")

                if os.path.isfile(f'content/{file_name}.txt'):

                    with open(f'content/{file_name}.txt', 'r', encoding='utf8') as file:

                        content = file.read().split('\n')

                    with open(f'content/{file_name}(decoded).txt', 'w', encoding='utf8') as file:

                        for line in content:

                            file.write((decode_full_shift_encryption(data["shift"], line)) + '\n')

                    print(f'\nФайл {file_name}(decoded).txt успешно создан')

                    return

                else:

                    print('Файл не найден')

                    continue

        case "manual":

            string = input("\nВведите строку: ")

            print(decode_full_shift_encryption(data["shift"], string))

            return
