import json


def config_user(id_config, name_config, where_get_data, encoding_or_decoding):

    encryption_symbols = input("\nВведите словарь в формате: ''' a:b, g:o, y:p ''': ")

    while True:

        escape_symbol = input('\nВведите символ для экранирования: ')

        if not len(escape_symbol) == 1:

            print('The length of the argument "escape_symbol" must be equal to one')

            continue

        else:

            config = {

                "id": id_config,
                "method_encryption": "user encryption",
                "encode/decode": encoding_or_decoding,
                "encryption_symbols": encryption_symbols,
                "escape_symbol": escape_symbol,
                "where_get_data": where_get_data,

            }

            with open('configs.json', 'r+') as file:

                file_data = json.load(file)

                file_data[name_config] = config

                file.seek(0)

                json.dump(file_data, file, indent=4)

            break
