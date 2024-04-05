from shift_encryption.shift_encryption import encode_shift_encryption, decode_shift_encryption


def helper_encode_file_input(file_content: list, file_locate: str) -> None:

    while True:

        save_register: str = input('\nKeep the register?(0 - no, 1 - yes): ')

        if save_register not in ['0', '1']:

            print('The input data can only be 0 or 1')

            continue

        else:

            break

    while True:

        try:

            shift: int = int(input('\nEnter the shift: '))

            if not 0 < shift < 27:

                raise TypeError

        except (TypeError, ValueError):

            print('The data type of the "shift" argument can only be an integer in interval [1; 26]')

            continue

        else:

            with open(f'content/{file_locate}(encoded).txt', 'w', encoding='utf8') as file:

                for line in file_content:

                    file.write((encode_shift_encryption(shift, line, bool(int(save_register)))) + '\n')

            print(f'\nFile "{file_locate}(encoded).txt" successfully created')

            break


def helper_decode_file_input(file_content: list, file_locate: str) -> None:

    while True:

        save_register: str = input('\nKeep the register?(0 - no, 1 - yes): ')

        if save_register not in ['0', '1']:

            print('The input data can only be 0 or 1')

            continue

        else:

            break

    while True:

        try:

            shift: int = int(input('\nEnter the shift: '))

            if not 0 < shift < 27:

                raise TypeError

        except (TypeError, ValueError):

            print('The data type of the "shift" argument can only be an integer in interval [1; 26]')

            continue

        else:

            with open(f'content/{file_locate}(decoded).txt', 'w', encoding='utf8') as file:

                for line in file_content:

                    file.write((decode_shift_encryption(shift, line, bool(int(save_register)))) + '\n')

            print(f'\nFile "{file_locate}(decoded).txt" successfully created')

            break
