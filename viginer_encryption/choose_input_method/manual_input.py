from viginer_encryption.viginer_encryption import (
    encode_viginer_encryption,
    decode_viginer_encryption,
)


def helper_encode_manual_input() -> str:
    string: str = input("\nEnter the text: ")

    while True:
        key_word: str = input("\nEnter the passphrase: ")

        if not all(
            [
                not (min([ord(x) for x in key_word]) < 97),
                key_word.islower(),
                not (max([ord(x) for x in key_word]) > 122),
            ]
        ):
            print(
                "Argument key_word must be in lowercase and contain only letters of the alphabet"
            )

            continue

        else:
            break

    while True:
        save_register: str = input("\nKeep the register?(0 - no, 1 - yes): ")

        if save_register not in ["0", "1"]:
            print("Input data can be only 1 or 0")

            continue

        else:
            return encode_viginer_encryption(string, key_word, bool(int(save_register)))


def helper_decode_manual_input() -> str:
    string: str = input("\nEnter the text: ")

    while True:
        key_word: str = input("\nEnter the passphrase: ")

        if not all(
            [
                not (min([ord(x) for x in key_word]) < 97),
                key_word.islower(),
                not (max([ord(x) for x in key_word]) > 122),
            ]
        ):
            print(
                "Argument key_word must be in lowercase and contain only letters of the alphabet"
            )

            continue

        else:
            break

    while True:
        save_register: str = input("\nKeep the register?(0 - no, 1 - yes): ")

        if save_register not in ["0", "1"]:
            print("Input data can be only 1 or 0")

            continue

        else:
            return decode_viginer_encryption(string, key_word, bool(int(save_register)))
