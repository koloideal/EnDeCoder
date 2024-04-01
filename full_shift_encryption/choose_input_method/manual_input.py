from full_shift_encryption.full_shift_encryption import encode_full_shift_encryption, decode_full_shift_encryption


def helper_encode_manual_input() -> str:

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

            return encode_full_shift_encryption(shift, string)


def helper_decode_manual_input() -> str:

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

            return decode_full_shift_encryption(shift, string)
