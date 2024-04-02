from shift_encryption.shift_encryption import encode_shift_encryption, decode_shift_encryption


def helper_encode_manual_input() -> str:

    while True:

        save_register = input("\nСохранять регистр?(0 - нет, 1 - да): ")

        if save_register not in ['0', '1']:

            print('Входные данные могут быть только 0 или 1')

            continue

        else:

            break

    string = input("\nВведите строку: ")

    while True:

        try:

            shift = int(input("\nВведите сдвиг: "))

            if not 0 < shift < 27:

                raise TypeError

        except (TypeError, ValueError):

            print('The data type of the "shift" argument can only be an integer in interval [1; 26]')

            continue

        else:

            return encode_shift_encryption(shift, string, bool(int(save_register)))


def helper_decode_manual_input() -> str:

    while True:

        save_register = input("\nСохранять регистр?(0 - нет, 1 - да): ")

        if save_register not in ['0', '1']:

            print('Входные данные могут быть только 0 или 1')

            continue

        else:

            break

    string = input("\nВведите строку: ")

    while True:

        try:

            shift = int(input("\nВведите сдвиг: "))

            if not 0 < shift < 27:

                raise TypeError

        except (TypeError, ValueError):

            print('The data type of the "shift" argument can only be an integer in interval [1; 26]')

            continue

        else:

            return decode_shift_encryption(shift, string, bool(int(save_register)))
