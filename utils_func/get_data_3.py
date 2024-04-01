import helper
import json
from utils_func.action_0_data_3 import action_0_data_3


def get_data_3():

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

            action = int(input('Enter action(0, to add a config or config id): '))

        except ValueError:

            print('Config not find\n')

            continue

        if action == 0:

            action_0_data_3()

            break

        else:

            be_config = False

            for config in configs:

                if configs[config]["id"] == int(action):

                    print(f'\nConfig "{config}" is selected')

                    be_config = True

                    break

            if not be_config:

                print('Config not find\n')

            else:

                break
