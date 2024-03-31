from atbash_encryption.atbash_encryption import encode_atbash_encryption, decode_atbash_encryption


def help_encode_atbash(file_content: list = None, file_locate: str = None) -> str or None:

    if file_content:

        while True:

            save_register = input("\nСохранять регистр?(0 - нет, 1 - да): ")

            if save_register not in ['0', '1']:

                print('Входные данные могут быть только 0 или 1')

                continue

            else:

                with open(f'content/{file_locate}(encoded).txt', 'w', encoding='utf8') as file:

                    for line in file_content:

                        file.write(encode_atbash_encryption(line, bool(int(save_register))) + '\n')

                print(f'\nФайл {file_locate}(encoded).txt успешно создан')

                break

    else:

        string = input("\nВведите строку: ")

        while True:

            save_register = input("\nСохранять регистр?(0 - нет, 1 - да): ")

            if save_register not in ['0', '1']:

                print('Входные данные могут быть только 0 или 1')

                continue

            else:

                return f'\nresult## {encode_atbash_encryption(string, bool(int(save_register)))}'


def help_decode_atbash(file_content: list = None, file_locate: str = None) -> str or None:

    if file_content:

        while True:

            save_register = input("\nСохранять регистр?(0 - нет, 1 - да): ")

            if save_register not in ['0', '1']:

                print('Входные данные могут быть только 0 или 1')

                continue

            else:

                with open(f'content/{file_locate}(decoded).txt', 'w', encoding='utf8') as file:

                    for line in file_content:

                        file.write(decode_atbash_encryption(line, bool(int(save_register))) + '\n')

                print(f'\nФайл {file_locate}(decoded).txt успешно создан')

                break

    else:

        string = input("\nВведите строку: ")

        while True:

            save_register = input("\nСохранять регистр?(0 - нет, 1 - да): ")

            if save_register not in ['0', '1']:

                print('Входные данные могут быть только 0 или 1')

                continue

            else:

                return f'\nresult## {decode_atbash_encryption(string, bool(int(save_register)))}'
