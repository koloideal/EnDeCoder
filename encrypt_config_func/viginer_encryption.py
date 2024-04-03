import json


def config_viginer(id_config, name_config, where_get_data, encoding_or_decoding):

    while True:

        key_word = input("\nВведите ключ-фразу: ")

        if not all([not (min([ord(x) for x in key_word]) < 97), key_word.islower(),
                    not (max([ord(x) for x in key_word]) > 122)]):

            print('Argument key_word must be in lowercase and contain only letters of the alphabet')

            continue

        else:

            break

    while True:

        save_register = input("\nСохранять регистр?(0 - нет, 1 - да) ")

        if save_register not in ['0', '1']:

            print('Input data can be only 1 or 0')

            continue

        else:

            save_register = bool(int(save_register))

            config = {

                "id": id_config,
                "method_encryption": "viginer encryption",
                "encode/decode": encoding_or_decoding,
                "save_register": save_register,
                "key_word": key_word,
                "where_get_data": where_get_data,

            }

            with open('configs.json', 'r+') as file:

                file_data = json.load(file)

                file_data[name_config] = config

                file.seek(0)

                json.dump(file_data, file, indent=4)

            break
