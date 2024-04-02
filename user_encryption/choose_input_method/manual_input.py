from user_encryption.user_encryption import encode_user_encryption, decode_user_encryption


def helper_encode_manual_input() -> str:

    encryption_symbols_str = input("\nВведите словарь в формате: ''' a:b, g:o, y:p ''': ")

    encryption_symbols = {}

    for i in encryption_symbols_str.split(','):

        encryption_symbols[i.replace(' ', '')[0]] = i.replace(' ', '')[2]

    string = input("\nВведите строку: ")

    while True:

        escape_symbol = input('\nВведите символ для экранирования: ')

        if not len(escape_symbol) == 1:

            print('The length of the argument "escape_symbol" must be equal to one')

            continue

        else:

            return encode_user_encryption(encryption_symbols, string, escape_symbol)


def helper_decode_manual_input() -> str:

    encryption_symbols_str = input("\nВведите словарь в формате: ''' a:b, g:o, y:p ''': ")

    encryption_symbols = {}

    for i in encryption_symbols_str.split(','):

        encryption_symbols[i.replace(' ', '')[0]] = i.replace(' ', '')[2]

    string = input("\nВведите строку: ")

    while True:

        escape_symbol = input('\nВведите символ для экранирования: ')

        if not len(escape_symbol) == 1:

            print('The length of the argument "escape_symbol" must be equal to one')

            continue

        else:

            return decode_user_encryption(encryption_symbols, string, escape_symbol)
