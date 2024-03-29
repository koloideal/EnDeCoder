import shift_encryption
import full_shift_encryption
import user_encryption
import atbash_encryption
import viginer_encryption
import full_viginer_encryption


def helper() -> str:

    dict_with_name_func = {

        1: 'shift_encryption',
        2: 'full_shift_encryption',
        3: 'user_encryption',
        4: 'atbash_encryption',
        5: 'viginer_encryption',
        6: 'full_viginer_encryption'

    }

    second_dict_with_name_func = {

        1: shift_encryption,
        2: full_shift_encryption,
        3: user_encryption,
        4: atbash_encryption,
        5: viginer_encryption,
        6: full_viginer_encryption

    }

    where_get_data = int(input('Здравствуй, выбери откуда кодировать/декодировать текст?(Введи цифру)\n'
                           '1. Из файла\n'
                           '2. Набрать вручную\n'))

    if where_get_data == 2:

        print('\nВыбери способ шифровки/дешифровки текста(Введи цифру)\n')

        for k, i in dict_with_name_func.items():

            print(f'{k}: {i}')

        encryption_method = input()

        encoding_or_decoding = int(input('Необходимо шифровать или расшифровать текст?(Введи цифру)\n'
                                     '1. Шифровать\n'
                                     '2. Расшифровать\n'))

        match encoding_or_decoding:

            case 1:

                pass


