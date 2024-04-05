import helper
from atbash_encryption.atbash_encryption import encode_atbash_encryption, decode_atbash_encryption
from full_shift_encryption.full_shift_encryption import encode_full_shift_encryption, decode_full_shift_encryption
from full_viginer_encryption.full_viginer_encryption import encode_full_viginer_encryption, decode_full_viginer_encryption
from shift_encryption.shift_encryption import encode_shift_encryption, decode_shift_encryption
from user_encryption.user_encryption import encode_user_encryption, decode_user_encryption
from viginer_encryption.viginer_encryption import encode_viginer_encryption, decode_viginer_encryption


name_func_to_func: dict = {

        'shift encryption': [encode_shift_encryption, decode_shift_encryption],
        'full shift encryption': [encode_full_shift_encryption, decode_full_shift_encryption],
        'user encryption': [encode_user_encryption, decode_user_encryption],
        'atbash encryption': [encode_atbash_encryption, decode_atbash_encryption],
        'viginer encryption': [encode_viginer_encryption, decode_viginer_encryption],
        'full viginer encryption': [encode_full_viginer_encryption, decode_full_viginer_encryption]

    }

name_funcs: dict = {

        1: 'shift encryption',
        2: 'full shift encryption',
        3: 'user encryption',
        4: 'atbash encryption',
        5: 'viginer encryption',
        6: 'full viginer encryption'

    }


def get_help() -> None:

    print('\nSelect the function or enter "stop" to exit the menu, to get help on the operation of the encryption '
          'method, you must enter its serial number point zero or one, 0 to get help on the encryption function, '
          '1 for the decryption function, the final type of request must be in this format: 1.0 , 2.1 , 6.0 , etc .\n')

    for k, i in enumerate(name_func_to_func.keys()):

        print(f'{k + 1}: {i}\n')

    while True:

        name_func: str = input('Enter a query or "stop": ')

        if name_func[0] not in ['1', '2', '3', '4', '5', '6'] and name_func != 'stop':

            print('Incorrect input\n')

            continue

        elif name_func[-1] not in ['0', '1'] and name_func != 'stop':

            print('Incorrect input\n')

            continue

        elif len(name_func) != 3 and name_func != 'stop':

            print('Incorrect input\n')

            continue

        else:

            if name_func == 'stop':

                print('\nReturn to the action selection mode\n')

                break

            else:

                match name_func[-1]:

                    case '0':

                        print(f'\nDescription of the encode function of the method {name_funcs[int(name_func[0])]}\n')

                        print(name_func_to_func[name_funcs[int(name_func[0])]][0].__doc__.replace('   ', ''))

                        print()

                    case '1':

                        print(f'\nDescription of the decode function of the method {name_funcs[int(name_func[0])]}\n')

                        print(name_func_to_func[name_funcs[int(name_func[0])]][1].__doc__.replace('   ', ''))

                        print()

                continue

    helper.helper()

    return
