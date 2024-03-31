from viginer_encryption.viginer_encryption import encode_viginer_encryption, decode_viginer_encryption


def help_encode_viginer(file_content: list = None, file_name: str = None) -> str or None:

    if file_content:

        while True:

            key_word = input("\nВведите ключ-фразу: ")

            if not all([not (min([ord(x) for x in key_word]) < 97), key_word.islower(),
                        not (max([ord(x) for x in key_word]) > 122)]):

                print('Argument key_word must be in lowercase and contain only letters of the alphabet')

                continue

            else:

                break

        while True:

            save_register = input("\nСохранять регистр?(0 - нет, 1 - да) ")

            if save_register not in ['0', '1']:

                print('Input data can be only 1 or 0')

                continue

            else:

                list_with_len_lines = [len(line) for line in file_content]

                encoded_string = encode_viginer_encryption(''.join(file_content), key_word, bool(int(save_register)))

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

        string = input("\nВведите строку: ")

        while True:

            key_word = input("\nВведите ключ-фразу: ")

            if not all([not (min([ord(x) for x in key_word]) < 97), key_word.islower(),
                        not (max([ord(x) for x in key_word]) > 122)]):

                print('Argument key_word must be in lowercase and contain only letters of the alphabet')

                continue

            else:

                break

        while True:

            save_register = input("\nСохранять регистр?(0 - нет, 1 - да) ")

            if save_register not in ['0', '1']:

                print('Input data can be only 1 or 0')

                continue

            else:

                return f'\nresult## {encode_viginer_encryption(string, key_word, bool(int(save_register)))}'


def help_decode_viginer(file_content: list = None, file_name: str = None) -> str or None:

    if file_content:

        while True:

            key_word = input("\nВведите ключ-фразу: ")

            if not all([not (min([ord(x) for x in key_word]) < 97), key_word.islower(),
                        not (max([ord(x) for x in key_word]) > 122)]):

                print('Argument key_word must be in lowercase and contain only letters of the alphabet')

                continue

            else:

                break

        while True:

            save_register = input("\nСохранять регистр?(0 - нет, 1 - да) ")

            if save_register not in ['0', '1']:

                print('Input data can be only 1 or 0')

                continue

            else:

                list_with_len_lines = [len(line) for line in file_content]

                decoded_string = decode_viginer_encryption(''.join(file_content), key_word, bool(int(save_register)))

                result_list = []

                long = 0

                for line in list_with_len_lines:

                    result_list.append(decoded_string[long:line + long])

                    long += line

                with open(f'content/{file_name}(decoded).txt', 'w', encoding='utf8') as file:

                    for line in result_list:

                        file.write(line + '\n')

                print(f'\nФайл {file_name}(decoded).txt успешно создан')

                break

    else:

        string = input("\nВведите строку: ")

        while True:

            key_word = input("\nВведите ключ-фразу: ")

            if not all([not (min([ord(x) for x in key_word]) < 97), key_word.islower(),
                        not (max([ord(x) for x in key_word]) > 122)]):

                print('Argument key_word must be in lowercase and contain only letters of the alphabet')

                continue

            else:

                break

        while True:

            save_register = input("\nСохранять регистр?(0 - нет, 1 - да) ")

            if save_register not in ['0', '1']:

                print('Input data can be only 1 or 0')

                continue

            else:

                return f'\nresult## {decode_viginer_encryption(string, key_word, bool(int(save_register)))}'
