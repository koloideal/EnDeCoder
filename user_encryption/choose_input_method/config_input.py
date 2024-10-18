from user_encryption.user_encryption import (
    encode_user_encryption,
    decode_user_encryption,
)
import os


def helper_encode_config_input(data: dict) -> None:
    match data["where_get_data"]:
        case "file":
            while True:
                file_name: str = input(
                    "\nEnter the name of the file without the extension: "
                )

                if os.path.isfile(f"content/{file_name}.txt"):
                    with open(f"content/{file_name}.txt", "r", encoding="utf8") as file:
                        content: list = file.read().split("\n")

                    encryption_symbols: dict = {}

                    for i in data["encryption_symbols"].split(","):
                        encryption_symbols[i.replace(" ", "")[0]] = i.replace(" ", "")[
                            2
                        ]

                    with open(
                        f"content/{file_name}(encoded).txt", "w", encoding="utf8"
                    ) as file:
                        for line in content:
                            file.write(
                                encode_user_encryption(
                                    encryption_symbols, line, data["escape_symbol"]
                                )
                                + "\n"
                            )

                    print(f'\nFile "{file_name}(encoded).txt" successfully created')

                    return

                else:
                    print("File was not found")

                    continue

        case "manual":
            encryption_symbols: dict = {}

            for i in data["encryption_symbols"].split(","):
                encryption_symbols[i.replace(" ", "")[0]] = i.replace(" ", "")[2]

            string: str = input("\nEnter the text: ")

            print(
                encode_user_encryption(
                    encryption_symbols, string, data["escape_symbol"]
                )
            )

            return


def helper_decode_config_input(data: dict) -> None:
    match data["where_get_data"]:
        case "file":
            while True:
                file_name: str = input(
                    "\nEnter the name of the file without the extension: "
                )

                if os.path.isfile(f"content/{file_name}.txt"):
                    with open(f"content/{file_name}.txt", "r", encoding="utf8") as file:
                        content: list = file.read().split("\n")

                    encryption_symbols: dict = {}

                    for i in data["encryption_symbols"].split(","):
                        encryption_symbols[i.replace(" ", "")[0]] = i.replace(" ", "")[
                            2
                        ]

                    with open(
                        f"content/{file_name}(decoded).txt", "w", encoding="utf8"
                    ) as file:
                        for line in content:
                            file.write(
                                decode_user_encryption(
                                    encryption_symbols, line, data["escape_symbol"]
                                )
                                + "\n"
                            )

                    print(f'\nFile "{file_name}(decoded).txt" successfully created')

                    return

                else:
                    print("File was not found")

                    continue

        case "manual":
            encryption_symbols: dict = {}

            for i in data["encryption_symbols"].split(","):
                encryption_symbols[i.replace(" ", "")[0]] = i.replace(" ", "")[2]

            string: str = input("\nEnter the text: ")

            print(
                decode_user_encryption(
                    encryption_symbols, string, data["escape_symbol"]
                )
            )

            return
