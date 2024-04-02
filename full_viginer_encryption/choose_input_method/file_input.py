from full_viginer_encryption.full_viginer_encryption import encode_full_viginer_encryption, decode_full_viginer_encryption


def helper_encode_file_input(file_content: list, file_locate: str) -> None:

    key_word = input("\nВведите ключ-фразу: ")

    list_with_len_lines = [len(line) for line in file_content]

    encoded_string = encode_full_viginer_encryption(''.join(file_content), key_word)

    result_list = []

    long = 0

    for line in list_with_len_lines:

        result_list.append(encoded_string[long:line + long])

        long += line

    with open(f'content/{file_locate}(encoded).txt', 'w', encoding='utf8') as file:

        for line in result_list:

            file.write(line + '\n')

    print(f'\nФайл {file_locate}(encoded).txt успешно создан')


def helper_decode_file_input(file_content: list, file_locate: str) -> None:

    key_word = input("\nВведите ключ-фразу: ")

    list_with_len_lines = [len(line) for line in file_content]

    decoded_string = decode_full_viginer_encryption(''.join(file_content), key_word)

    result_list = []

    long = 0

    for line in list_with_len_lines:

        result_list.append(decoded_string[long:line + long])

        long += line

    with open(f'content/{file_locate}(decoded).txt', 'w', encoding='utf8') as file:

        for line in result_list:

            file.write(line + '\n')

    print(f'\nФайл {file_locate}(decoded).txt успешно создан')
