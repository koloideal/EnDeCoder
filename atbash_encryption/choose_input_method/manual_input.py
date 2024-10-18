from atbash_encryption.atbash_encryption import (
    encode_atbash_encryption,
    decode_atbash_encryption,
)


def helper_encode_manual_input() -> str:
    string: str = input("\nEnter the text: ")

    while True:
        save_register: str = input("\nKeep the register?(0 - no, 1 - yes): ")

        if save_register not in ["0", "1"]:
            print("The input data can only be 0 or 1")

            continue

        else:
            return encode_atbash_encryption(string, bool(int(save_register)))


def helper_decode_manual_input() -> str:
    string: str = input("\nEnter the text: ")

    while True:
        save_register: str = input("\nKeep the register?(0 - no, 1 - yes): ")

        if save_register not in ["0", "1"]:
            print("The input data can only be 0 or 1")

            continue

        else:
            return decode_atbash_encryption(string, bool(int(save_register)))
