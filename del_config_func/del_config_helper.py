import json
import helper


def del_config():

    with open("configs.json", "r", encoding='utf8') as config_file:

        configs = json.load(config_file)

    print('\nРежим удаления конфигурации')

    for k, config in enumerate(configs):

        print(f'{k + 1}.\tname : {config}')

        for j in configs[config]:

            print(f'\t{j} : {configs[config][j]}')

        print()

    while True:

        name_config = input('\nВведи название конфигурации для удаления\n')

        if name_config not in configs:

            print('Такого конфига не существует')

            continue

        elif name_config in ['config_1', 'config_2']:

            print('Вы не можете удалить дефолтные конфиги')

            continue

        else:

            with open('configs.json', 'r+', encoding='utf8') as config_file:

                configs = json.load(config_file)

                configs.pop(name_config)

            with open('configs.json', 'w', encoding='utf8') as file:

                json.dump(configs, file, indent=4)

            print(f'\nКонфиг "{name_config}" удалён\n')

            print('Возврат в режим выбора действий\n')

            helper.helper()
