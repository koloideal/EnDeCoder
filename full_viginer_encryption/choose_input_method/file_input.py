from full_viginer_encryption.full_viginer_encryption import (
    encode_full_viginer_encryption,
    decode_full_viginer_encryption,
)


def helper_encode_file_input(file_content: list, file_locate: str) -> None:
    key_word: str = input("\nEnter the passphrase: ")

    list_with_len_lines: list = [len(line) for line in file_content]

    encoded_string: str = encode_full_viginer_encryption(
        "".join(file_content), key_word
    )

    result_list: list = []

    long: int = 0

    for line in list_with_len_lines:
        result_list.append(encoded_string[long : line + long])

        long += line

    with open(f"content/{file_locate}(encoded).txt", "w", encoding="utf8") as file:
        for line in result_list:
            file.write(line + "\n")

    print(f"\nFile {file_locate}(encoded).txt successfully created")

    return


def helper_decode_file_input(file_content: list, file_locate: str) -> None:
    key_word: str = input("\nEnter the passphrase: ")

    list_with_len_lines: list = [len(line) for line in file_content]

    decoded_string: str = decode_full_viginer_encryption(
        "".join(file_content), key_word
    )

    result_list: list = []

    long: int = 0

    for line in list_with_len_lines:
        result_list.append(decoded_string[long : line + long])

        long += line

    with open(f"content/{file_locate}(decoded).txt", "w", encoding="utf8") as file:
        for line in result_list:
            file.write(line + "\n")

    print(f'\nFile "{file_locate}(decoded).txt" successfully created')

    return
