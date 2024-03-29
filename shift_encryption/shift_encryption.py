from shift_encryption.get_chr_for_shift import get_chr_encode, get_chr_decode
import datetime


def encode_shift_encryption(shift: int, string: str, save_register: bool = False) -> str:

    """ This encryption function takes shift, string and save_register as arguments and returns an encrypted string;
    the essence of encryption is that each character of the transmitted string is replaced by a character whose
    ordinal number is equal to the ordinal number of the original character plus the value of the "shift" argument,
    that is, the so-called "shift" occurs in accordance with the ASCII table; the value of the "shift" argument can
    only be an integer in the range (0; 27), if the value goes beyond this encryption interval, this is abnormal and,
    most likely, the text will not be able to be decrypted, the value of the "string" argument can only be a string,
    while each ordinal number of the character in the argument should not go beyond the interval [65; 90] && [97;
    122], all characters coming out of this interval will be ignored during encryption, but in the output line they
    will remain in the same places where they were in the original line; if the value of the save_register argument
    is True, the case of all characters in the output string will be the same as the corresponding characters in the
    source string, it is important: the number of characters in the transmitted and output strings is always the
    same! """

    try:

        result_chr: list = []

        for i in [(ord(x) - 96) if (96 < ord(x) < 123) else x for x in string.lower()]:

            if isinstance(i, int):

                result_chr.append(get_chr_encode(shift, i))

            else:

                result_chr.append(i)

        result: str = ''

        if save_register:

            for k, i in enumerate(result_chr):

                if i.islower() and string[k].islower():

                    result += i

                else:

                    result += i.upper()

            return result

        else:

            result = ''.join(result_chr)

            return result

    except Exception as e:

        with open('traceback.txt', 'a', encoding='utf8') as traceback:

            traceback.write(f'Error: {e}\nDatetime: {datetime.datetime.now()}\n\n')

        raise type(e)(e)


def decode_shift_encryption(shift: int, string: str, save_register: bool = False) -> str:

    """ This decryption function takes shift, string and save_register as arguments and returns the decrypted string;
    the essence of decryption is that each character of the transmitted string is replaced by a character whose
    ordinal number is equal to the ordinal number of the original character minus the value of the "shift" argument,
    that is, the so-called "shift" occurs in accordance with the ASCII table; the value of the "shift" argument can
    only be an integer in the range (0; 27), the value of the "string" argument can only be a string,
    and each ordinal number of the character in the argument must not exceed the interval [65; 90] && [97; 122],
    all characters coming out of this interval will be ignored during encryption, but they will remain the same in
    the output string the places where they were in the source string; if the value of the save_register argument is
    True, the case of all characters in the output string will be the same as the corresponding characters in the
    source string, it is important: the number of characters in the transmitted and output strings is always the
    same! """

    try:

        result_chr: list = []

        for i in [(ord(x) - 96) if (96 < ord(x) < 123) else x for x in string.lower()]:

            if isinstance(i, int):

                result_chr.append(get_chr_decode(shift, i))

            else:

                result_chr.append(i)

        result: str = ''

        if save_register:

            for k, i in enumerate(result_chr):

                if i.islower() and string[k].islower():

                    result += i

                else:

                    result += i.upper()

            return result

        else:

            result = ''.join(result_chr)

            return result

    except Exception as e:

        with open('traceback.txt', 'a', encoding='utf8') as traceback:

            traceback.write(f'Error: {e}\nDatetime: {datetime.datetime.now()}\n\n')

        raise type(e)(e)
