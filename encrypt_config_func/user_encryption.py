import json


def config_user(
    id_config: int, name_config: str, where_get_data: str, encoding_or_decoding: str
) -> None:
    encryption_symbols: str = input(
        '\nEnter the dictionary in the format: """ a:b, g:o, y:p """: '
    )

    while True:
        escape_symbol: str = input("\nEnter the character to escape: ")

        if not len(escape_symbol) == 1:
            print('The length of the argument "escape_symbol" must be equal to one')

            continue

        else:
            config: json = {
                "id": id_config,
                "method_encryption": "user encryption",
                "encode/decode": encoding_or_decoding,
                "encryption_symbols": encryption_symbols,
                "escape_symbol": escape_symbol,
                "where_get_data": where_get_data,
            }

            with open("configs.json", "r+", encoding="utf8") as file:
                file_data: json = json.load(file)

                file_data[name_config]: json = config

                file.seek(0)

                json.dump(file_data, file, indent=4)

            break
