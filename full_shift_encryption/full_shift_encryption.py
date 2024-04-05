import datetime


def encode_full_shift_encryption(shift: int, string: str) -> str:

    """ This encryption function takes a shift and a string as arguments and returns an encrypted string; the essence
    of encryption is that each character of the transmitted string is replaced by a character whose ordinal number
    is equal to the ordinal number of the original character plus the value of the argument "shift", that is,
    the so-called "shift" occurs according to the ASCII table; the value of the argument "the shift" can only be an
    integer in the interval (0; 95), if the value goes beyond this encryption interval is abnormal and most likely
    will not be able to be decrypted, the value of the "string" argument can only be a string, while each ordinal
    number of the character in the argument should not go beyond the interval [32; 126]; important: the number of
    characters in the transmitted and output strings It's always the same! """

    try:

        return ''.join([chr(x) for x in [(ord(j) + shift) if 31 < (ord(j) + shift) < 127 else (ord(j) + shift + 94) if (ord(j) < 31) else (ord(j) + shift - 94) for j in string]])

    except Exception as e:

        with open('traceback.txt', 'a', encoding='utf8') as traceback:

            traceback.write(f'Error: {e}\nDatetime: {datetime.datetime.now()}\n\n')

        raise type(e)(e)


def decode_full_shift_encryption(shift: int, string: str) -> str:

    """ This decryption function takes a shift and a string as arguments and returns the decrypted string; the essence
    of decryption is that each character of the transmitted string is replaced by a character whose ordinal number is
    equal to the ordinal number of the original character minus the value of the argument "shift", that is,
    the so-called "shift" occurs according to the ASCII table; the value of the argument "the shift" can only be an
    integer in the interval (0; 95), if the value goes beyond this interval, the encryption is abnormal and most
    likely will not be able to be decrypted, the value of the "string" argument can only be a string, while each
    ordinal number of the character in the argument should not go beyond the interval [32; 126]; important: the
    number of characters in the transmitted and output lines are always equal! """

    try:

        return ''.join([chr(x) for x in [(ord(j) - shift) if 31 < (ord(j) - shift) < 127 else (ord(j) - shift - 94) if (ord(j) < 31) else (ord(j) - shift + 94) for j in string]])

    except Exception as e:

        with open('traceback.txt', 'a', encoding='utf8') as traceback:

            traceback.write(f'Error: {e}\nDatetime: {datetime.datetime.now()}\n\n')

        raise type(e)(e)
