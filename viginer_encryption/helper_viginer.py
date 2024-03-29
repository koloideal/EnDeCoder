from viginer_encryption.viginer_encryption import encode_viginer_encryption, decode_viginer_encryption


def help_encode_viginer():

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


def help_decode_viginer():

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
