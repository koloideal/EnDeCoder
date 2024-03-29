from atbash_encryption.atbash_encryption import encode_atbash_encryption, decode_atbash_encryption


def help_encode_atbash():

    while True:

        string = input("\nВведите строку: ")

        save_register = input("\nСохранять регистр?(0 - нет, 1 - да): ")

        if not isinstance(string, str) or save_register not in ['0', '1']:

            print('Входные данные могут быть только 0 или 1')

            continue

        else:

            return f'\nresult## {encode_atbash_encryption(string, bool(int(save_register)))}'


def help_decode_atbash():

    while True:

        string = input("\nВведите строку: ")

        save_register = input("\nСохранять регистр?(0 - нет, 1 - да): ")

        if not isinstance(string, str) or save_register not in ['0', '1']:

            print('Входные данные могут быть только 0 или 1')

            continue

        else:

            return f'\nresult## {decode_atbash_encryption(string, bool(int(save_register)))}'
