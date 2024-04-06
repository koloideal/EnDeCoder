import datetime
import os
from get_data_func.get_data_file import get_data_file
from get_data_func.get_data_manual import get_data_manual
from get_data_func.get_data_config import get_data_config
from help_func.get_help import get_help
from atbash_encryption.helper_atbash import help_encode_atbash, help_decode_atbash
from user_encryption.helper_user import help_encode_user, help_decode_user
from full_shift_encryption.helper_full_shift import help_encode_full_shift, help_decode_full_shift
from shift_encryption.helper_shift import help_encode_shift, help_decode_shift
from full_viginer_encryption.helper_full_viginer import help_encode_full_viginer, help_decode_full_viginer
from viginer_encryption.helper_viginer import help_encode_viginer, help_decode_viginer

name_func: dict = {

    1: 'shift encryption',
    2: 'full shift encryption',
    3: 'user encryption',
    4: 'atbash encryption',
    5: 'viginer encryption',
    6: 'full viginer encryption'

}

name_func_to_func: dict = {

    1: [help_encode_shift, help_decode_shift],
    2: [help_encode_full_shift, help_decode_full_shift],
    3: [help_encode_user, help_decode_user],
    4: [help_encode_atbash, help_decode_atbash],
    5: [help_encode_viginer, help_decode_viginer],
    6: [help_encode_full_viginer, help_decode_full_viginer]

}


def helper() -> None:

    os.makedirs('content', exist_ok=True)

    with open('configs.json', 'a', encoding='utf-8'):

        pass

    while True:

        where_get_data: str = input('\nHello, choose where to encode/decode text from?(Enter a number)\n\n'
                                    '0. Get help on encryption methods\n'
                                    '1. From the file\n'
                                    '2. Typing manually\n'
                                    '3. Select a saved configuration\n')

        if where_get_data not in ['0', '1', '2', '3']:

            continue

        else:

            break

    if where_get_data == '1':

        get_data_file()

    elif where_get_data == '2':

        get_data_manual()

    elif where_get_data == '3':

        get_data_config()

    else:

        get_help()

    helper()
