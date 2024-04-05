import json


def config_viginer(id_config: int, name_config: str, where_get_data: str, encoding_or_decoding: str) -> None:

    while True:

        key_word: str = input("\nEnter the passphrase: ")

        if not all([not (min([ord(x) for x in key_word]) < 97), key_word.islower(),
                    not (max([ord(x) for x in key_word]) > 122)]):

            print('Argument key_word must be in lowercase and contain only letters of the alphabet')

            continue

        else:

            break

    while True:

        save_register: str = input('\nKeep the register?(0 - no, 1 - yes): ')

        if save_register not in ['0', '1']:

            print('Input data can be only 1 or 0')

            continue

        else:

            save_register: bool = bool(int(save_register))

            config: json = {

                "id": id_config,
                "method_encryption": "viginer encryption",
                "encode/decode": encoding_or_decoding,
                "save_register": save_register,
                "key_word": key_word,
                "where_get_data": where_get_data,

            }

            with open('configs.json', 'r+', encoding='utf8') as file:

                file_data: json = json.load(file)

                file_data[name_config]: json = config

                file.seek(0)

                json.dump(file_data, file, indent=4)

            break
