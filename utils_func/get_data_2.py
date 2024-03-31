import helper


def get_data_2():

    while True:

        print('\nВыбери способ шифровки/дешифровки текста(Введи цифру)')

        for k, i in helper.dict_with_name_func.items():
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

            print(helper.second_dict_with_name_func[int(encryption_method)][0]())

        case '2':

            print(helper.second_dict_with_name_func[int(encryption_method)][1]())
