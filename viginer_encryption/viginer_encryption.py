from viginer_encryption.get_chr_for_viginer import get_chr_encode, get_chr_decode
import datetime


def encode_viginer_encryption(string: str, key_word: str, save_register: bool = False) -> str:

    """ This encryption function takes a "string" and a "passphrase" as arguments and returns an encrypted string; the
    essence of encryption is that each character of the transmitted string is replaced by a character whose ordinal
    number is equal to the ordinal number of the original character plus the ordinal number of the corresponding
    character from the passphrase, that is, the so-called "shift" according to with an ASCII table; value the
    arguments "string" and "passphrase" can only be a string, while each ordinal number of a character in
    "passphrase" must be in the interval [97; 122], only the letters of the alphabet are encrypted, all other
    characters will be ignored, but at the same time they will be in the same places in the output string where they
    were in the original string; important: the number of characters in the transmitted and output strings is always
    the same! """

    try:

        first_step_list: list = []

        for i in [(ord(x) - 96) if (96 < ord(x) < 123) else x for x in string.lower()]:

            first_step_list.append(i)

        key_word_list = [ord(x) - 96 for x in key_word]

        result = get_chr_encode(first_step_list, key_word_list, save_register, string)

        return result

    except Exception as e:

        with open('traceback.txt', 'a', encoding='utf8') as traceback:

            traceback.write(f'Error: {e}\nDatetime: {datetime.datetime.now()}\n\n')

        raise type(e)(e)


def decode_viginer_encryption(string: str, key_word: str, save_register: bool = False) -> str:

    """ This decryption function takes a "string" and a "passphrase" as arguments and returns the decrypted string;
    the essence of decryption is that each character of the transmitted string is replaced by a character whose
    ordinal number is equal to the ordinal number of the original character minus the ordinal number of the
    corresponding character from the passphrase, that is, the so-called "shift" according to with an ASCII table; the
    value of the arguments "string" and "passphrase" can only be a string, while each character sequence number in
    "passphrase" must be in the interval [97; 122], only the letters of the alphabet are decrypted, all other
    characters will be ignored, but at the same time they will be in the same places in the output string where they
    were in the original string; important: the number of characters in the transmitted and output strings is always
    the same! """

    try:

        first_step_list: list = []

        for i in [(ord(x) - 96) if (96 < ord(x) < 123) else x for x in string.lower()]:

            first_step_list.append(i)

        key_word_list = [ord(x) - 96 for x in key_word]

        result = get_chr_decode(first_step_list, key_word_list, save_register, string)

        return result

    except Exception as e:

        with open('traceback.txt', 'a', encoding='utf8') as traceback:

            traceback.write(f'Error: {e}\nDatetime: {datetime.datetime.now()}\n\n')

        raise type(e)(e)
