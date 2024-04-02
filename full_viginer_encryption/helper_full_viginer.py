from full_viginer_encryption.choose_input_method.file_input import helper_encode_file_input, helper_decode_file_input
from full_viginer_encryption.choose_input_method.manual_input import helper_encode_manual_input, helper_decode_manual_input


def help_encode_full_viginer(file_content: list = None, file_locate: str = None) -> str or None:

    if file_content:

        helper_encode_file_input(file_content, file_locate)

    else:

        return helper_encode_manual_input()


def help_decode_full_viginer(file_content: list = None, file_locate: str = None) -> str or None:

    if file_content:

        helper_decode_file_input(file_content, file_locate)

    else:

        return helper_decode_manual_input()
