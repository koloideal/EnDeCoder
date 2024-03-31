from full_viginer_encryption.full_viginer_encryption import encode_full_viginer_encryption, decode_full_viginer_encryption


def help_encode_full_viginer(file_content: list = None, file_locate: str = None) -> str or None:

    if file_content:

        key_word = input("\nВведите ключ-фразу: ")

        new_file_content = chr(127).join(file_content)

        with open(f'content/{file_locate}(encoded).txt', 'w', encoding='utf8') as file:

            for line in file_content:

                file.write(encode_full_viginer_encryption(line, key_word=key_word) + '\n')

        print(f'\nФайл {file_locate}(encoded).txt успешно создан')

    else:

        string = input("\nВведите строку: ")

        key_word = input("\nВведите ключ-фразу: ")

        return f'\nresult## {encode_full_viginer_encryption(string, key_word=key_word)}'


def help_decode_full_viginer(file_content: list = None, file_locate: str = None) -> str or None:

    if file_content:

        key_word = input("\nВведите ключ-фразу: ")

        with open(f'content/{file_locate}(decoded).txt', 'w', encoding='utf8') as file:

            for line in file_content:
                file.write(decode_full_viginer_encryption(line, key_word=key_word) + '\n')

        print(f'\nФайл {file_locate}(decoded).txt успешно создан')

    else:

        string = input("\nВведите строку: ")

        key_word = input("\nВведите ключ-фразу: ")

        return f'\nresult## {decode_full_viginer_encryption(string, key_word=key_word)}'
