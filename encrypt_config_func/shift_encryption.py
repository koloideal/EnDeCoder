import json


def config_shift(id_config, name_config, where_get_data, encoding_or_decoding):

    while True:

        save_register = input("\nСохранять регистр?(0 - нет, 1 - да): ")

        if save_register not in ['0', '1']:

            print('Входные данные могут быть только 0 или 1')

            continue

        else:

            save_register = bool(int(save_register))

            break

    while True:

        try:

            shift = int(input("\nВведите сдвиг: "))

            if not 0 < shift < 27:

                raise TypeError

        except (TypeError, ValueError):

            print('The data type of the "shift" argument can only be an integer in interval [1; 26]')

            continue

        else:

            break

    config = {

        "id": id_config,
        "method_encryption": "shift encryption",
        "encode/decode": encoding_or_decoding,
        "shift": shift,
        "save_register": save_register,
        "where_get_data": where_get_data,

    }

    with open('configs.json', 'r+') as file:

        file_data = json.load(file)

        file_data[name_config] = config

        file.seek(0)

        json.dump(file_data, file, indent=4)
