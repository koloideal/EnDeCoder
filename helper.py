import datetime
import os
from get_data_func.get_data_file import get_data_file
from get_data_func.get_data_manual import get_data_manual
from get_data_func.get_data_config import get_data_config
from atbash_encryption.helper_atbash import help_encode_atbash, help_decode_atbash
from user_encryption.helper_user import help_encode_user, help_decode_user
from full_shift_encryption.helper_full_shift import help_encode_full_shift, help_decode_full_shift
from shift_encryption.helper_shift import help_encode_shift, help_decode_shift
from full_viginer_encryption.helper_full_viginer import help_encode_full_viginer, help_decode_full_viginer
from viginer_encryption.helper_viginer import help_encode_viginer, help_decode_viginer


name_func = {

        1: 'shift encryption',
        2: 'full shift encryption',
        3: 'user encryption',
        4: 'atbash encryption',
        5: 'viginer encryption',
        6: 'full viginer encryption'

    }

name_func_to_func = {

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

    with open('traceback.txt', 'a', encoding='utf8') as traceback:

        traceback.write(f'Start logging, datetime: {datetime.datetime.now()}\n\n')

    while True:

        where_get_data = input('Здравствуй, выбери откуда кодировать/декодировать текст?(Введи цифру)\n'
                               '1. Из файла\n'
                               '2. Набрать вручную\n'
                               '3. Выбрать сохранённую конфигурацию\n')

        if where_get_data not in ['1', '2', '3']:

            continue

        else:

            break

    if where_get_data == '1':

        get_data_file()

    elif where_get_data == '2':

        get_data_manual()

    else:

        get_data_config()
