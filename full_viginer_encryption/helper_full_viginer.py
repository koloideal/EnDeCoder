from full_viginer_encryption.full_viginer_encryption import encode_full_viginer_encryption, decode_full_viginer_encryption


def help_encode_full_viginer():

    while True:

        string = input("\nВведите строку: ")

        key_word = input("\nВведите ключ-фразу: ")

        return f'\nresult## {encode_full_viginer_encryption(string, key_word=key_word)}'


def help_decode_full_viginer():

    while True:

        string = input("\nВведите строку: ")

        key_word = input("\nВведите ключ-фразу: ")

        return f'\nresult## {decode_full_viginer_encryption(string, key_word=key_word)}'
