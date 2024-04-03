import json


def config_full_viginer(id_config, name_config, where_get_data, encoding_or_decoding):

    key_word = input("\nВведите ключ-фразу: ")

    config = {

        "id": id_config,
        "method_encryption": "full viginer encryption",
        "encode/decode": encoding_or_decoding,
        "key_word": key_word,
        "where_get_data": where_get_data,

    }

    with open('configs.json', 'r+') as file:

        file_data = json.load(file)

        file_data[name_config] = config

        file.seek(0)

        json.dump(file_data, file, indent=4)
