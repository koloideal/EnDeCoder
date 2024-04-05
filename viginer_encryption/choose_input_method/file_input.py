from viginer_encryption.viginer_encryption import encode_viginer_encryption, decode_viginer_encryption


def helper_encode_file_input(file_content: list, file_name: str) -> None:

    while True:

        key_word: str = input('\nEnter the passphrase: ')

        if not all([not (min([ord(x) for x in key_word]) < 97), key_word.islower(),
                    not (max([ord(x) for x in key_word]) > 122)]):

            print('Argument key_word must be in lowercase and contain only letters of the alphabet')

            continue

        else:

            break

    while True:

        save_register: str = input('\nKeep the register?(0 - no, 1 - yes): ')

        if save_register not in ['0', '1']:

            print('Input data can be only 1 or 0')

            continue

        else:

            list_with_len_lines: list = [len(line) for line in file_content]

            encoded_string: str = encode_viginer_encryption(''.join(file_content), key_word, bool(int(save_register)))

            result_list: list = []

            long: int = 0

            for line in list_with_len_lines:

                result_list.append(encoded_string[long:line + long])

                long += line

            with open(f'content/{file_name}(encoded).txt', 'w', encoding='utf8') as file:

                for line in result_list:

                    file.write(line + '\n')

            print(f'\nFile "{file_name}(encoded).txt" successfully created')

            break


def helper_decode_file_input(file_content: list, file_name: str) -> None:

    while True:

        key_word: str = input('\nEnter the passphrase: ')

        if not all([not (min([ord(x) for x in key_word]) < 97), key_word.islower(),
                    not (max([ord(x) for x in key_word]) > 122)]):

            print('Argument key_word must be in lowercase and contain only letters of the alphabet')

            continue

        else:

            break

    while True:

        save_register: str = input('\nKeep the register?(0 - no, 1 - yes): ')

        if save_register not in ['0', '1']:

            print('Input data can be only 1 or 0')

            continue

        else:

            list_with_len_lines: list = [len(line) for line in file_content]

            decoded_string: str = decode_viginer_encryption(''.join(file_content), key_word, bool(int(save_register)))

            result_list: list = []

            long: int = 0

            for line in list_with_len_lines:

                result_list.append(decoded_string[long:line + long])

                long += line

            with open(f'content/{file_name}(decoded).txt', 'w', encoding='utf8') as file:

                for line in result_list:

                    file.write(line + '\n')

            print(f'\nFile "{file_name}(decoded).txt" successfully created')

            break
