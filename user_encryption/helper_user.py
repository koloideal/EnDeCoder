from user_encryption.user_encryption import encode_user_encryption, decode_user_encryption


def help_encode_user():

    while True:

        encryption_symbols_str = input("\nВведите словарь в формате: ''' a:b, g:o, y:p ''': ")

        encryption_symbols = {}

        for i in encryption_symbols_str.split(', '):

            encryption_symbols[i[0]] = i[2]

        string = input("\nВведите строку: ")

        escape_symbol = input('\nВведите символ для экранирования: ')

        if not len(escape_symbol) == 1:

            print('The data type of the "encryption_symbols" argument can only be an dictionary'
                  ', and the data type of the argument "string" can only be a string, the length of the '
                  'argument "escape_symbol" must be equal to one')

            continue

        else:

            return f'\nresult## {encode_user_encryption(encryption_symbols, string, escape_symbol)}'


def help_decode_user():

    while True:

        encryption_symbols_str = input("\nВведите словарь в формате: ''' a:b, g:o, y:p ''': ")

        encryption_symbols = {}

        for i in encryption_symbols_str.split(', '):

            encryption_symbols[i[0]] = i[2]

        string = input("\nВведите строку: ")

        escape_symbol = input('\nВведите символ для экранирования: ')

        if not len(escape_symbol) == 1:

            print('The data type of the "encryption_symbols" argument can only be an dictionary'
                  ', and the data type of the argument "string" can only be a string, the length of the '
                  'argument "escape_symbol" must be equal to one')

            continue

        else:

            return f'\nresult## {decode_user_encryption(encryption_symbols, string, escape_symbol)}'
