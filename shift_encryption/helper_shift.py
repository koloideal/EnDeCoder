from shift_encryption.shift_encryption import encode_shift_encryption, decode_shift_encryption


def help_encode_shift(file_content: list = None, file_locate: str = None) -> str or None:

    if file_content:

        while True:

            save_register = input("\nСохранять регистр?(0 - нет, 1 - да): ")

            if save_register not in ['0', '1']:

                print('Входные данные могут быть только 0 или 1')

                continue

            try:

                shift = int(input("\nВведите сдвиг: "))

                if not 0 < shift < 27:

                    raise TypeError

            except (TypeError, ValueError):

                print('The data type of the "shift" argument can only be an integer in interval [1; 26]')

                continue

            else:

                with open(f'content/{file_locate}(encoded).txt', 'w', encoding='utf8') as file:

                    for line in file_content:

                        file.write((encode_shift_encryption(shift, line, bool(int(save_register)))) + '\n')

                print(f'\nФайл {file_locate}(encoded).txt успешно создан')

                break

    else:

        while True:

            save_register = input("\nСохранять регистр?(0 - нет, 1 - да): ")

            if save_register not in ['0', '1']:

                print('Входные данные могут быть только 0 или 1')

                continue

            string = input("\nВведите строку: ")

            try:

                shift = int(input("\nВведите сдвиг: "))

                if not 0 < shift < 27:

                    raise TypeError

            except (TypeError, ValueError):

                print('The data type of the "shift" argument can only be an integer in interval [1; 26]')

                continue

            else:

                return f'\nresult## {encode_shift_encryption(shift, string, bool(int(save_register)))}'


def help_decode_shift(file_content: list = None, file_locate: str = None) -> str or None:

    if file_content:

        while True:

            save_register = input("\nСохранять регистр?(0 - нет, 1 - да): ")

            if save_register not in ['0', '1']:

                print('Входные данные могут быть только 0 или 1')

                continue

            try:

                shift = int(input("\nВведите сдвиг: "))

                if not 0 < shift < 27:

                    raise TypeError

            except (TypeError, ValueError):

                print('The data type of the "shift" argument can only be an integer in interval [1; 26]')

                continue

            else:

                with open(f'content/{file_locate}(decoded).txt', 'w', encoding='utf8') as file:

                    for line in file_content:

                        file.write((decode_shift_encryption(shift, line, bool(int(save_register)))) + '\n')

                print(f'\nФайл {file_locate}(decoded).txt успешно создан')

                break

    else:

        while True:

            save_register = input("\nСохранять регистр?(0 - нет, 1 - да): ")

            if save_register not in ['0', '1']:

                print('Входные данные могут быть только 0 или 1')

                continue

            string = input("\nВведите строку: ")

            try:

                shift = int(input("\nВведите сдвиг: "))

                if not 0 < shift < 27:

                    raise TypeError

            except (TypeError, ValueError):

                print('The data type of the "shift" argument can only be an integer in interval [1; 26]')

                continue

            else:

                return f'\nresult## {decode_shift_encryption(shift, string, bool(int(save_register)))}'
