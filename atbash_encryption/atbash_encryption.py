from atbash_encryption.get_chr_for_atbash import get_chr
import datetime


def encode_atbash_encryption(string: str, save_register: bool = False) -> str:

    """ This encryption function takes a string as an argument and returns an encrypted string; the essence of
    encryption is that each letter of the transmitted string is replaced by a "mirror" letter in the alphabet,
    that is: the letter "a" is replaced by "z", "b" by "y", and so on, in in a formulaic form, it looks like this: &"
    -> 26 - &', where &" is the ordinal number of the letter of the transmitted string, and &' is the ordinal number
    of the letter of the output string; all non-alphabetic characters, that is, characters in between [0; 65) && (90;
    97) && (122; 127] in the ASCII table, during encryption and decryption, they will be ignored and will not be
    encrypted, but at the same time in the output line they will remain in the same places where they were in the
    function has a second optional argument save_register, the default value is False,with this value the case of the
    output string will be converted to the lower case, if the argument is True, the case of each letter
    of the letter in the output string will correspond to the case of the letter in the transmitted string;
    important: the number of characters in the transmitted and output strings is always equal! """

    try:

        first_list_of_ords = [(ord(x) - 96) if 96 < ord(x) < 123 else x for x in string.lower()]

        second_list_of_ords = [(27 - x) if isinstance(x, int) else x for x in first_list_of_ords]

        third_list_of_ords = get_chr(second_list_of_ords)

        if save_register:

            fourth_list_of_ords = []

            for k, i in enumerate(third_list_of_ords):

                if i.islower() and string[k].islower():

                    fourth_list_of_ords.append(i)

                else:

                    fourth_list_of_ords.append(i.upper())

            return ''.join(fourth_list_of_ords)

        else:

            return ''.join(third_list_of_ords)

    except Exception as e:

        with open('traceback.txt', 'a', encoding='utf8') as traceback:

            traceback.write(f'Error: {e}\nDatetime: {datetime.datetime.now()}\n\n')

        raise type(e)(e)


def decode_atbash_encryption(string: str, save_register: bool = False) -> str:

    """This decryption function takes an encrypted string as an argument and returns the decrypted
    string; the essence of decryption is that each letter of the transmitted string is replaced by a "mirror" letter
    in the alphabet, that is: the letter "a" is replaced by "z", "b" by "y", and so on, in the template the form it
    looks like this: &" -> 26 - &', where &" is the ordinal number of the letter of the transmitted string,
    and &' is the ordinal number of the letter of the output string; all non-alphabetic characters, that is,
    characters between [0; 65) && (90; 97) && (122; 127] in the ASCII table, during encryption and decryption,
    they will be ignored and will not be encrypted, but at the same time in the output string they will remain in the
    same places where they were in the transmitted string; the function has a second optional argument save_register,
    the default value is False, with this value the case of the output string will be converted to the lower case
    case, if the argument is True, then the case of each letter in the output string will correspond to the case of
    the corresponding letter in the transmitted string; important: the number of characters in the transmitted and
    output strings is always equal!"""

    return encode_atbash_encryption(string, save_register)
