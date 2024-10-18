from full_viginer_encryption.get_chr_for_full_viginer import (
    get_chr_encode,
    get_chr_decode,
)
import datetime


def encode_full_viginer_encryption(string: str, key_word: str) -> str:
    """This encryption function takes a "string" and a "passphrase" as arguments and returns an encrypted string; the
    essence of encryption is that each character of the transmitted string is replaced by a character whose ordinal
    number is equal to the ordinal number of the original character plus the ordinal number of the corresponding
    character from the passphrase, that is, the so-called "shift" according to the ASCII table; the value of the
    arguments "string" and "passphrase" can only be a string, while each ordinal number of the character in the
    arguments must not exceed the interval [32; 126]; important: the number of characters in the transmitted and
    output strings is always the same!"""

    try:
        first_step_list: list = [ord(x) - 31 for x in string]

        key_word_list: list = [ord(x) - 31 for x in key_word]

        result: str = get_chr_encode(first_step_list, key_word_list)

        return result

    except Exception as e:
        with open("traceback.txt", "a", encoding="utf8") as traceback:
            traceback.write(f"Error: {e}\nDatetime: {datetime.datetime.now()}\n\n")

        raise type(e)(e)


def decode_full_viginer_encryption(string: str, key_word: str) -> str:
    """This decryption function takes a "string" and a "passphrase" as arguments and returns the decrypted string;
    the essence of decryption is that each character of the transmitted string is replaced by a character whose
    ordinal number is equal to the ordinal number of the original character minus the ordinal number of the
    corresponding character from the passphrase, that is, the so-called "shift" according to the ASCII table; the
    value of the arguments "string" and "passphrase" can only be a string, while each ordinal number of the character
    in the arguments must not exceed the interval [32; 126]; important: the number of characters in the transmitted
    and output strings is always the same!"""

    try:
        first_step_list: list = [ord(x) - 31 for x in string]

        key_word_list: list = [ord(x) - 31 for x in key_word]

        result: str = get_chr_decode(first_step_list, key_word_list)

        return result

    except Exception as e:
        with open("traceback.txt", "a", encoding="utf8") as traceback:
            traceback.write(f"Error: {e}\nDatetime: {datetime.datetime.now()}\n\n")

        raise type(e)(e)
