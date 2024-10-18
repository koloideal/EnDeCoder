import json


def config_full_viginer(
    id_config: int, name_config: str, where_get_data: str, encoding_or_decoding: str
) -> None:
    key_word: str = input("\nEnter the passphrase: ")

    config: json = {
        "id": id_config,
        "method_encryption": "full viginer encryption",
        "encode/decode": encoding_or_decoding,
        "key_word": key_word,
        "where_get_data": where_get_data,
    }

    with open("configs.json", "r+", encoding="utf8") as file:
        file_data: json = json.load(file)

        file_data[name_config]: json = config

        file.seek(0)

        json.dump(file_data, file, indent=4)
