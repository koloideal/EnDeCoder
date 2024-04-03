import helper
from encrypt_config_func.user_encryption import config_user
from encrypt_config_func.full_viginer_encryption import config_full_viginer
from encrypt_config_func.viginer_encryption import config_viginer
from encrypt_config_func.shift_encryption import config_shift
from encrypt_config_func.atbash_encryption import config_atbash
from encrypt_config_func.full_shift_encryption import config_full_shift
import json


def add_config() -> None:

    with open("configs.json", "r", encoding='utf8') as config_file:

        configs = json.load(config_file)

        id_config = max([configs[x]["id"] for x in configs]) + 1

    print('\nРежим добавления конфигурации')

    while True:

        name_config = input('\nВведи название конфигурации\n')

        if name_config not in configs:

            break

        else:

            print('Конфиг уже существует')

            continue

    while True:

        str_get_data = input('\nВыбери источник данных(Введи цифру)\n'
                             '1. Ручной ввод\n'
                             '2. Файл\n')

        where_get_data = 'manual' if str_get_data == '1' else 'file' if str_get_data == '2' else None

        if not where_get_data:

            continue

        else:

            break

    while True:

        print('\nВыбери способ шифровки/дешифровки текста(Введи цифру)')

        for k, i in helper.name_func.items():

            print(f'{k}. {i}')

        encryption_method = input()

        if encryption_method not in ['1', '2', '3', '4', '5', '6']:

            continue

        else:

            break

    while True:

        encode_decode = input('\nНеобходимо шифровать или расшифровать текст?(Введи цифру)\n'
                              '1. Шифровать\n'
                              '2. Расшифровать\n')

        if encode_decode not in ['1', '2']:

            continue

        else:

            encode_decode = 'encode' if encode_decode == '1' else 'decode' if encode_decode == '2' else None

            break

    match encryption_method:

        case '1':

            config_shift(id_config, name_config, where_get_data, encode_decode)

        case '2':

            config_full_shift(id_config, name_config, where_get_data, encode_decode)

        case '3':

            config_user(id_config, name_config, where_get_data, encode_decode)

        case '4':

            config_atbash(id_config, name_config, where_get_data, encode_decode)

        case '5':

            config_viginer(id_config, name_config, where_get_data, encode_decode)

        case '6':

            config_full_viginer(id_config, name_config, where_get_data, encode_decode)
