import json
from add_config_func.add_config_helper import add_config
from del_config_func.del_config_helper import del_config
from atbash_encryption.helper_atbash import help_encode_atbash, help_decode_atbash
from user_encryption.helper_user import help_encode_user, help_decode_user
from full_shift_encryption.helper_full_shift import help_encode_full_shift, help_decode_full_shift
from shift_encryption.helper_shift import help_encode_shift, help_decode_shift
from full_viginer_encryption.helper_full_viginer import help_encode_full_viginer, help_decode_full_viginer
from viginer_encryption.helper_viginer import help_encode_viginer, help_decode_viginer


name_func = {

    'shift encryption': [help_encode_shift, help_decode_shift],
    'full shift encryption': [help_encode_full_shift, help_decode_full_shift],
    'user encryption': [help_encode_user, help_decode_user],
    'atbash encryption': [help_encode_atbash, help_decode_atbash],
    'viginer encryption': [help_encode_viginer, help_decode_viginer],
    'full viginer encryption': [help_encode_full_viginer, help_decode_full_viginer]

    }


def get_data_config():

    with open('configs.json', 'r', encoding='utf8') as config_file:

        configs = json.load(config_file)

        print()

        for k, config in enumerate(configs):

            print(f'{k + 1}.\tname : {config}')

            for j in configs[config]:

                print(f'\t{j} : {configs[config][j]}')

            print()

    while True:

        try:

            action: str = input('Enter(0, to add config, -0 to delete config or config id): ')

            int_action: int = int(action)

        except ValueError:

            print('Config not find\n')

            continue

        if int_action == 0 and action != '-0':

            add_config()

            return

        elif action == '-0':

            del_config()

            return

        else:

            be_config: bool = False

            for config in configs:

                if configs[config]["id"] == int_action:

                    print(f'\nConfig "{config}" is selected')

                    data = {}

                    for single_data in configs[config]:

                        data[single_data] = configs[config][single_data]

                    be_config = True

                    break

            if not be_config:

                print('Config not find\n')

            else:

                break

    match data["encode/decode"]:

        case "encode":

            name_func[data["method_encryption"]][0](data=data)

        case "decode":

            name_func[data["method_encryption"]][1](data=data)
