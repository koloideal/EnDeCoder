import json


def config_full_shift(id_config: int, name_config: str, where_get_data: str, encoding_or_decoding: str) -> None:

    while True:

        try:

            shift: int = int(input('\nEnter the shift: '))

            if not 0 < shift < 27:

                raise TypeError

        except (TypeError, ValueError):

            print('The data type of the "shift" argument can only be an integer in interval [1; 26]')

            continue

        else:

            config: json = {

                "id": id_config,
                "method_encryption": "full shift encryption",
                "encode/decode": encoding_or_decoding,
                "shift": shift,
                "where_get_data": where_get_data,

            }

            with open('configs.json', 'r+', encoding='utf8') as file:

                file_data: json = json.load(file)

                file_data[name_config]: json = config

                file.seek(0)

                json.dump(file_data, file, indent=4)

            break
