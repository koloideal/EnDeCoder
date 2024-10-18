from full_viginer_encryption.full_viginer_encryption import (
    encode_full_viginer_encryption,
    decode_full_viginer_encryption,
)


def helper_encode_manual_input() -> str:
    string: str = input("\nEnter the text: ")

    key_word: str = input("\nEnter the passphrase: ")

    return encode_full_viginer_encryption(string, key_word=key_word)


def helper_decode_manual_input() -> str:
    string: str = input("\nEnter the text: ")

    key_word: str = input("\nEnter the passphrase: ")

    return decode_full_viginer_encryption(string, key_word=key_word)
