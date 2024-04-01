from atbash_encryption.atbash_encryption import encode_atbash_encryption, decode_atbash_encryption


def helper_encode_manual_input() -> str or None:

    string = input("\nВведите строку: ")

    while True:

        save_register = input("\nСохранять регистр?(0 - нет, 1 - да): ")

        if save_register not in ['0', '1']:

            print('Входные данные могут быть только 0 или 1')

            continue

        else:

            return encode_atbash_encryption(string, bool(int(save_register)))


def helper_decode_manual_input() -> str or None:

    string = input("\nВведите строку: ")

    while True:

        save_register = input("\nСохранять регистр?(0 - нет, 1 - да): ")

        if save_register not in ['0', '1']:

            print('Входные данные могут быть только 0 или 1')

            continue

        else:

            return decode_atbash_encryption(string, bool(int(save_register)))
