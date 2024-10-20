from full_shift_encryption.choose_input_method.file_input import (
    helper_encode_file_input,
    helper_decode_file_input,
)
from full_shift_encryption.choose_input_method.manual_input import (
    helper_encode_manual_input,
    helper_decode_manual_input,
)
from full_shift_encryption.choose_input_method.config_input import (
    helper_encode_config_input,
    helper_decode_config_input,
)


def help_encode_full_shift(
    file_content: list = None, file_locate: str = None, data: dict = None
) -> str or None:
    if file_content and not data:
        helper_encode_file_input(file_content, file_locate)

    elif data and not file_content:
        helper_encode_config_input(data)

    else:
        return helper_encode_manual_input()


def help_decode_full_shift(
    file_content: list = None, file_locate: str = None, data: dict = None
) -> str or None:
    if file_content and not data:
        helper_decode_file_input(file_content, file_locate)

    elif data and not file_content:
        helper_decode_config_input(data)

    else:
        return helper_decode_manual_input()
