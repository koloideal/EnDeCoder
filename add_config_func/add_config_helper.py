import helper
from encrypt_config_func.user_encryption import config_user
from encrypt_config_func.full_viginer_encryption import config_full_viginer
from encrypt_config_func.viginer_encryption import config_viginer
from encrypt_config_func.shift_encryption import config_shift
from encrypt_config_func.atbash_encryption import config_atbash
from encrypt_config_func.full_shift_encryption import config_full_shift
import json


def add_config() -> None:
    with open("configs.json", "r", encoding="utf8") as config_file:
        configs: json = json.load(config_file)

        id_config: int = max([configs[x]["id"] for x in configs]) + 1

    print("\nConfiguration addition mode")

    while True:
        name_config: str = input("\nEnter name configuration\n")

        if (
            name_config not in configs
            and not name_config.endswith("(to_decode)")
            and not name_config.endswith("(to_encode)")
        ):
            break

        elif name_config.endswith("(to_decode)") or name_config.endswith("(to_encode)"):
            print("Invalid name")

            continue

        else:
            print("Config already exists")

            continue

    while True:
        str_get_data: str = input(
            "\nSelect a data source (Enter a number)\n" "1. Manual input\n" "2. File\n"
        )

        where_get_data: str or None = (
            "manual" if str_get_data == "1" else "file" if str_get_data == "2" else None
        )

        if not where_get_data:
            continue

        else:
            break

    while True:
        print("\nChoose a way to encrypt/decrypt the text (Enter a number)")

        for k, i in helper.name_func.items():
            print(f"{k}. {i}")

        encryption_method: str = input()

        if encryption_method not in ["1", "2", "3", "4", "5", "6"]:
            continue

        else:
            break

    while True:
        encode_decode: str = input(
            "\nDo I need to encrypt or decrypt the text?(Enter a number)\n"
            "1. Encrypt\n"
            "2. Decrypt\n"
        )

        if encode_decode not in ["1", "2"]:
            continue

        else:
            encode_decode: str or None = (
                "encode"
                if encode_decode == "1"
                else "decode"
                if encode_decode == "2"
                else None
            )

            break

    match encryption_method:
        case "1":
            config_shift(id_config, name_config, where_get_data, encode_decode)

        case "2":
            config_full_shift(id_config, name_config, where_get_data, encode_decode)

        case "3":
            config_user(id_config, name_config, where_get_data, encode_decode)

        case "4":
            config_atbash(id_config, name_config, where_get_data, encode_decode)

        case "5":
            config_viginer(id_config, name_config, where_get_data, encode_decode)

        case "6":
            config_full_viginer(id_config, name_config, where_get_data, encode_decode)

    with open("configs.json", "r+", encoding="utf8") as file:
        data: json = json.load(file)

        need_config: dict = data[name_config]

    mirror_config: dict = need_config

    mirror_config["encode/decode"]: str = (
        "encode" if need_config["encode/decode"] == "decode" else "decode"
    )

    mirror_config["id"]: int = need_config["id"] + 1

    with open("configs.json", "r+", encoding="utf8") as file:
        file_data: json = json.load(file)

        second_part_name: str = (
            "(to_encode)"
            if mirror_config["encode/decode"] == "encode"
            else "(to_decode)"
        )

        file_data[f"{name_config}{second_part_name}"]: json = mirror_config

        file.seek(0)

        json.dump(file_data, file, indent=4)

    print(f'\nConfig "{name_config}" generated\n')

    print("Return to the action selection mode\n")

    with open("traceback.txt", "a", encoding="utf8") as traceback:
        traceback.write("Successful configuration creation\n\n")

    helper.helper()

    return
