from viginer_encryption.viginer_encryption import encode_viginer_encryption, decode_viginer_encryption
import os


def helper_encode_config_input(data: dict) -> None:

    match data["where_get_data"]:

        case "file":

            while True:

                file_name = input("\nВведи название файла без расширения: ")

                if os.path.isfile(f'content/{file_name}.txt'):

                    with open(f'content/{file_name}.txt', 'r', encoding='utf8') as file:

                        content = file.read().split('\n')

                    list_with_len_lines = [len(line) for line in content]

                    encoded_string = encode_viginer_encryption(''.join(content), data["key_word"], data["save_register"])

                    result_list = []

                    long = 0

                    for line in list_with_len_lines:

                        result_list.append(encoded_string[long:line + long])

                        long += line

                    with open(f'content/{file_name}(encoded).txt', 'w', encoding='utf8') as file:

                        for line in result_list:

                            file.write(line + '\n')

                    print(f'\nФайл {file_name}(encoded).txt успешно создан')

                    break

                else:

                    print('Файл не найден')

                    continue

        case "manual":

            string = input("\nВведите строку: ")

            print(encode_viginer_encryption(string, data["key_word"], data["save_register"]))

            return


def helper_decode_config_input(data: dict) -> None:

    match data["where_get_data"]:

        case "file":

            while True:

                file_name = input("\nВведи название файла без расширения: ")

                if os.path.isfile(f'content/{file_name}.txt'):

                    with open(f'content/{file_name}.txt', 'r', encoding='utf8') as file:

                        content = file.read().split('\n')

                    list_with_len_lines = [len(line) for line in content]

                    encoded_string = decode_viginer_encryption(''.join(content), data["key_word"], data["save_register"])

                    result_list = []

                    long = 0

                    for line in list_with_len_lines:

                        result_list.append(encoded_string[long:line + long])

                        long += line

                    with open(f'content/{file_name}(decoded).txt', 'w', encoding='utf8') as file:

                        for line in result_list:

                            file.write(line + '\n')

                    print(f'\nФайл {file_name}(decoded).txt успешно создан')

                    break

                else:

                    print('Файл не найден')

                    continue

        case "manual":

            string = input("\nВведите строку: ")

            print(decode_viginer_encryption(string, data["key_word"], data["save_register"]))

            return
