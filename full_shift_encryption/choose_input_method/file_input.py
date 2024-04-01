from full_shift_encryption.full_shift_encryption import encode_full_shift_encryption, decode_full_shift_encryption


def helper_encode_file_input(file_content: list, file_locate: str) -> None:

    while True:

        try:

            shift = int(input("\nВведите сдвиг: "))

            if not 0 < shift < 27:

                raise TypeError

        except (TypeError, ValueError):

            print('The data type of the "shift" argument can only be an integer in interval [1; 26]')

            continue

        else:

            with open(f'content/{file_locate}(encoded).txt', 'w', encoding='utf8') as file:

                for line in file_content:

                    file.write((encode_full_shift_encryption(shift, line)) + '\n')

            print(f'\nФайл {file_locate}(encoded).txt успешно создан')

            break


def helper_decode_file_input(file_content: list, file_locate: str) -> None:

    while True:

        try:

            shift = int(input("\nВведите сдвиг: "))

            if not 0 < shift < 27:

                raise TypeError

        except (TypeError, ValueError):

            print('The data type of the "shift" argument can only be an integer in interval [1; 26]')

            continue

        else:

            with open(f'content/{file_locate}(decoded).txt', 'w', encoding='utf8') as file:

                for line in file_content:

                    file.write((decode_full_shift_encryption(shift, line)) + '\n')

            print(f'\nФайл {file_locate}(decoded).txt успешно создан')

            break
