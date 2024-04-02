from atbash_encryption.atbash_encryption import encode_atbash_encryption, decode_atbash_encryption
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

                            file.write(encode_atbash_encryption(line, data["save_register"]) + '\n')

                    print(f'\nФайл {file_name}(encoded).txt успешно создан')

                    return

                else:

                    print('Файл не найден')

                    continue

        case "manual":

            string = input("\nВведите строку: ")

            print(encode_atbash_encryption(string, data["save_register"]))

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
                            file.write(decode_atbash_encryption(line, data["save_register"]) + '\n')

                    print(f'\nФайл {file_name}(decoded).txt успешно создан')

                    return

                else:

                    print('Файл не найден')

                    continue

        case "manual":

            string = input("\nВведите строку: ")

            print(decode_atbash_encryption(string, data["save_register"]))

            return
