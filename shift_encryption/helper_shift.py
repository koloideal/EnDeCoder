from shift_encryption.shift_encryption import encode_shift_encryption, decode_shift_encryption


def help_encode_shift():

    while True:

        string = input("\nВведите строку: ")

        try:

            shift = int(input("\nВведите сдвиг: "))

            if not 0 < shift < 27:

                raise TypeError

        except (TypeError, ValueError):

            print('The data type of the "shift" argument can only be an integer in interval [1; 26]')

            continue

        return f'\nresult## {encode_shift_encryption(shift, string)}'


def help_decode_shift():

    while True:

        string = input("\nВведите строку: ")

        try:

            shift = int(input("\nВведите сдвиг: "))

            if not 0 < shift < 27:

                raise TypeError

        except (TypeError, ValueError):

            print('The data type of the "shift" argument can only be an integer in interval [1; 26]')

            continue

        return f'\nresult## {decode_shift_encryption(shift, string)}'
