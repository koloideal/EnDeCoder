from atbash_encryption.helper_atbash import help_encode_atbash, help_decode_atbash
from user_encryption.helper_user import help_encode_user, help_decode_user
from full_shift_encryption.helper_full_shift import help_encode_full_shift, help_decode_full_shift
from shift_encryption.helper_shift import help_encode_shift, help_decode_shift
from full_viginer_encryption.helper_full_viginer import help_encode_full_viginer, help_decode_full_viginer
from viginer_encryption.helper_viginer import help_encode_viginer, help_decode_viginer


def helper() -> None:

    dict_with_name_func = {

        1: 'shift encryption',
        2: 'full shift encryption',
        3: 'user encryption',
        4: 'atbash encryption',
        5: 'viginer encryption',
        6: 'full viginer encryption'

    }

    second_dict_with_name_func = {

        1: [help_encode_shift, help_decode_shift],
        2: [help_encode_full_shift, help_decode_full_shift],
        3: [help_encode_user, help_decode_user],
        4: [help_encode_atbash, help_decode_atbash],
        5: [help_encode_viginer, help_decode_viginer],
        6: [help_encode_full_viginer, help_decode_full_viginer]

    }

    where_get_data = int(input('Здравствуй, выбери откуда кодировать/декодировать текст?(Введи цифру)\n'
                               '1. Из файла\n'
                               '2. Набрать вручную\n'))

    if where_get_data == 2:

        print('\nВыбери способ шифровки/дешифровки текста(Введи цифру)')

        for k, i in dict_with_name_func.items():

            print(f'{k}. {i}')

        encryption_method = int(input())

        encoding_or_decoding = int(input('\nНеобходимо шифровать или расшифровать текст?(Введи цифру)\n'
                                         '1. Шифровать\n'
                                         '2. Расшифровать\n'))

        match encoding_or_decoding:

            case 1:

                print(second_dict_with_name_func[encryption_method][0]())

            case 2:

                print(second_dict_with_name_func[encryption_method][1]())
