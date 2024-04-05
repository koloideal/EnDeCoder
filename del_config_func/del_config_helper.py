import json
import helper


def del_config() -> None:

    with open('configs.json', 'r', encoding='utf8') as config_file:

        configs: json = json.load(config_file)

    print('\nConfiguration deletion mode')

    while True:

        name_config: str = input('\nEnter the name of the configuration to delete\n')

        if name_config not in configs:

            print('There is no such config')

            continue

        elif name_config in ['config_1', 'config_2']:

            print('You cannot delete default configs')

            continue

        else:

            with open('configs.json', 'r+', encoding='utf8') as config_file:

                configs: json = json.load(config_file)

                configs.pop(name_config)

            with open('configs.json', 'w', encoding='utf8') as file:

                json.dump(configs, file, indent=4)

            print(f'\nConfig "{name_config}" has been deleted\n')

            print('Return to the action selection mode\n')

            break

    helper.helper()

    return
