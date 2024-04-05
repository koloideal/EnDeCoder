import json


def config_atbash(id_config: int, name_config: str, where_get_data: str, encoding_or_decoding: str) -> None:

    while True:

        save_register: str = input('\nKeep the register?(0 - no, 1 - yes): ')

        if save_register not in ['0', '1']:

            print('The input data can only be 0 or 1')

            continue

        else:

            save_register: bool = bool(int(save_register))

            config: json = {

                "id": id_config,
                "method_encryption": "atbash encryption",
                "encode/decode": encoding_or_decoding,
                "save_register": save_register,
                "where_get_data": where_get_data,

            }

            with open('configs.json', 'r+', encoding='utf8') as file:

                file_data: json = json.load(file)

                file_data[name_config]: json = config

                file.seek(0)

                json.dump(file_data, file, indent=4)

            break
