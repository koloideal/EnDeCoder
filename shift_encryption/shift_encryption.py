from shift_encryption.get_chr_for_shift import get_chr_encode, get_chr_decode


def encode_shift_encryption(shift: int, string: str, save_register: bool = False) -> str:

    if not isinstance(shift, int) or not isinstance(string, str) or not 0 < shift < 27:

        raise TypeError('The data type of the "shift" argument can only be an integer'
                        ', and the data type of the argument "string" can only be a string')

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

        raise type(e)(e)


def decode_shift_encryption(shift: int, string: str, save_register: bool = False) -> str:

    if not isinstance(shift, int) or not isinstance(string, str) or not 0 < shift < 27:

        raise TypeError('The data type of the "shift" argument can only be an integer'
                        ', and the data type of the argument "string" can only be a string')

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

        raise type(e)(e)
