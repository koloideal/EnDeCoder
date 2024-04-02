from user_encryption.user_encryption import encode_user_encryption, decode_user_encryption


def helper_encode_file_input(file_content: list, file_locate: str) -> None:

    encryption_symbols_str = input("\nВведите словарь в формате: ''' a:b, g:o, y:p ''': ")

    encryption_symbols = {}

    for i in encryption_symbols_str.split(','):

        encryption_symbols[i.replace(' ', '')[0]] = i.replace(' ', '')[2]

    while True:

        escape_symbol = input('\nВведите символ для экранирования: ')

        if not len(escape_symbol) == 1:

            print('The length of the argument "escape_symbol" must be equal to one')

            continue

        else:

            with open(f'content/{file_locate}(encoded).txt', 'w', encoding='utf8') as file:

                for line in file_content:

                    file.write(encode_user_encryption(encryption_symbols, line, escape_symbol) + '\n')

            print(f'\nФайл {file_locate}(encoded).txt успешно создан')

            break


def helper_decode_file_input(file_content: list, file_locate: str) -> None:

    encryption_symbols_str = input("\nВведите словарь в формате: ''' a:b, g:o, y:p ''': ")

    encryption_symbols = {}

    for i in encryption_symbols_str.split(','):
        encryption_symbols[i.replace(' ', '')[0]] = i.replace(' ', '')[2]

    while True:

        escape_symbol = input('\nВведите символ для экранирования: ')

        if not len(escape_symbol) == 1:

            print('The length of the argument "escape_symbol" must be equal to one')

            continue

        else:

            with open(f'content/{file_locate}(decoded).txt', 'w', encoding='utf8') as file:

                for line in file_content:

                    file.write(decode_user_encryption(encryption_symbols, line, escape_symbol) + '\n')

            print(f'\nФайл {file_locate}(decoded).txt успешно создан')

            break
