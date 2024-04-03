import helper


def get_data_manual():

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

        encoding_or_decoding = input('\nНеобходимо шифровать или расшифровать текст?(Введи цифру)\n'
                                     '1. Шифровать\n'
                                     '2. Расшифровать\n')

        if encoding_or_decoding not in ['1', '2']:

            continue

        else:

            break

    match encoding_or_decoding:

        case '1':

            print(helper.name_func_to_func[int(encryption_method)][0]())

        case '2':

            print(helper.name_func_to_func[int(encryption_method)][1]())
