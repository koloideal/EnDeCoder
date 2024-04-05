from atbash_encryption.atbash_encryption import encode_atbash_encryption, decode_atbash_encryption


def helper_encode_file_input(file_content: list, file_locate: str) -> None:

    while True:

        save_register: str = input('\nKeep the register?(0 - no, 1 - yes): ')

        if save_register not in ['0', '1']:

            print('The input data can only be 0 or 1')

            continue

        else:

            with open(f'content/{file_locate}(encoded).txt', 'w', encoding='utf8') as file:

                for line in file_content:

                    file.write(encode_atbash_encryption(line, bool(int(save_register))) + '\n')

            print(f'\nFile "{file_locate}(encoded).txt" successfully created')

            break


def helper_decode_file_input(file_content: list, file_locate: str) -> None:

    while True:

        save_register: str = input('\nKeep the register?(0 - no, 1 - yes): ')

        if save_register not in ['0', '1']:

            print('The input data can only be 0 or 1')

            continue

        else:

            with open(f'content/{file_locate}(decoded).txt', 'w', encoding='utf8') as file:

                for line in file_content:

                    file.write(decode_atbash_encryption(line, bool(int(save_register))) + '\n')

            print(f'\nFile {file_locate}(decoded).txt successfully created')

            break
