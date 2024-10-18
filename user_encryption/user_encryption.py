import datetime


def encode_user_encryption(
    encryption_symbols: dict, string: str, escape_symbol: str = "0"
) -> str:
    """This encryption function takes "string" and "dictionary" as arguments and returns an encrypted string; the
    essence of encryption is that each character of the transmitted string, if it is in the dictionary keys,
    is replaced by a character that is the value of this key; there is a third argument, optional: "escape_symbol,
    the default value of which is '0', the value of this argument will escape characters that are both in the source
    string and in the key values in the dictionary, this is necessary for correct decryption in the future,
    the value of the argument "escape_symbol" can only be a string consisting of one character ; the value the
    "string" argument can only be a string, the value of the "dictionary" argument can only be a dictionary,
    where both the key and the key value are a string consisting of a single character; in case of deviation from the
    above norms, the operation of the functions is abnormal, and bugs are very likely; important: the number of
    characters in the transmitted and output lines is always equal!; very important: the escape_symbol character
    MUST NOT BE CONTAINED in the input string, otherwise the behavior of the function cannot be predicted"""

    try:
        more_str: str = ""

        result: str = ""

        for i in string:
            if i in encryption_symbols.values():
                more_str += escape_symbol + i

            else:
                more_str += i

        for i in more_str:
            if i in encryption_symbols.keys():
                result += encryption_symbols[i]

            else:
                result += i

        return result

    except Exception as e:
        with open("traceback.txt", "a", encoding="utf8") as traceback:
            traceback.write(f"Error: {e}\nDatetime: {datetime.datetime.now()}\n\n")

        raise type(e)(e)


def decode_user_encryption(
    encryption_symbols: dict, string: str, escape_symbol: str = "0"
) -> str:
    """This decryption function takes "string" and "dictionary" as arguments and returns the decrypted string; the
    essence of decryption is that each character of the transmitted string, if it is in the dictionary keys,
    is replaced by a character that is the value of this key; there is a third argument, optional: "escape_symbol,
    the default value of which is equal to '0', the value of this argument will escape characters that are both in
    the source string and in the key values in the dictionary, the value of the argument "escape_symbol" can only be
    a string consisting of one character ; the value of the "string" argument can only be a string, the value of the
    "dictionary" argument can only be a dictionary, where both the key and the key value are a string consisting of
    one character; when deviating from the above norms, the operation of the functions is abnormal, and bugs are very
    likely; important: the number of characters in the transmitted and output strings It 's always the same !; very
    important: the escape_symbol character MUST NOT BE CONTAINED in the input string, otherwise the behavior of the
    function cannot be predicted"""

    try:
        result: str = ""

        for k, i in enumerate(string):
            if i in encryption_symbols.keys() and string[k - 1] != escape_symbol:
                result += encryption_symbols[i]

            elif i != escape_symbol:
                result += i

            else:
                continue

        return result

    except Exception as e:
        with open("traceback.txt", "a", encoding="utf8") as traceback:
            traceback.write(f"Error: {e}\nDatetime: {datetime.datetime.now()}\n\n")

        raise type(e)(e)
