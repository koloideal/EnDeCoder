from viginer_encryption.viginer_encryption import encode_viginer_encryption, decode_viginer_encryption


def help_encode_viginer(file_content: list = None, file_locate: str = None) -> str or None:

    if file_content:

        while True:

            key_word = input("\nВведите ключ-фразу: ")

            save_register = input("\nСохранять регистр?(0 - нет, 1 - да) ")

            if not all([not (min([ord(x) for x in key_word]) < 97), key_word.islower(),
                        not (max([ord(x) for x in key_word]) > 122), save_register in ['0', '1']]):
                print('The data type of the arguments "string" and "key_word" can only be a string;'
                      ' argument key_word must be in lowercase and contain only letters of the alphabet')

                continue

            else:

                with open(f'content/{file_locate}(encoded).txt', 'w', encoding='utf8') as file:

                    for line in file_content:

                        file.write(encode_viginer_encryption(line, key_word, bool(int(save_register))) + '\n')

                print(f'\nФайл {file_locate}(encoded).txt успешно создан')

                break

    else:

        while True:

            string = input("\nВведите строку: ")

            key_word = input("\nВведите ключ-фразу: ")

            save_register = input("\nСохранять регистр?(0 - нет, 1 - да) ")

            if not all([not (min([ord(x) for x in key_word]) < 97), key_word.islower(),
                        not (max([ord(x) for x in key_word]) > 122), save_register in ['0', '1']]):

                print('The data type of the arguments "string" and "key_word" can only be a string;'
                      ' argument key_word must be in lowercase and contain only letters of the alphabet')

                continue

            return f'\nresult## {encode_viginer_encryption(string, key_word, bool(int(save_register)))}'


def help_decode_viginer(file_content: list = None, file_locate: str = None) -> str or None:

    if file_content:

        while True:

            key_word = input("\nВведите ключ-фразу: ")

            save_register = input("\nСохранять регистр?(0 - нет, 1 - да) ")

            if not all([not (min([ord(x) for x in key_word]) < 97), key_word.islower(),
                        not (max([ord(x) for x in key_word]) > 122), save_register in ['0', '1']]):
                print('The data type of the arguments "string" and "key_word" can only be a string;'
                      ' argument key_word must be in lowercase and contain only letters of the alphabet')

                continue

            else:

                with open(f'content/{file_locate}(decoded).txt', 'w', encoding='utf8') as file:

                    for line in file_content:

                        file.write(decode_viginer_encryption(line, key_word, bool(int(save_register))) + '\n')

                print(f'\nФайл {file_locate}(decoded).txt успешно создан')

                break

    else:

        while True:

            string = input("\nВведите строку: ")

            key_word = input("\nВведите ключ-фразу: ")

            save_register = input("\nСохранять регистр?(0 - нет, 1 - да)")

            if not all([not (min([ord(x) for x in key_word]) < 97), key_word.islower(),
                        not (max([ord(x) for x in key_word]) > 122), save_register in ['0', '1']]):

                print('The data type of the arguments "string" and "key_word" can only be a string;'
                      ' argument key_word must be in lowercase and contain only letters of the alphabet')

                continue

            return f'\nresult## {decode_viginer_encryption(string, key_word, bool(int(save_register)))}'
