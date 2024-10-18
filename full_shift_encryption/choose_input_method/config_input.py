from full_shift_encryption.full_shift_encryption import (
    encode_full_shift_encryption,
    decode_full_shift_encryption,
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

                    with open(
                        f"content/{file_name}(encoded).txt", "w", encoding="utf8"
                    ) as file:
                        for line in content:
                            file.write(
                                (encode_full_shift_encryption(data["shift"], line))
                                + "\n"
                            )

                    print(f'\nFile "{file_name}(encoded).txt" successfully created')

                    return

                else:
                    print("The file was not found")

                    continue

        case "manual":
            string: str = input("\nEnter the text: ")

            print(encode_full_shift_encryption(data["shift"], string))

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

                    with open(
                        f"content/{file_name}(decoded).txt", "w", encoding="utf8"
                    ) as file:
                        for line in content:
                            file.write(
                                (decode_full_shift_encryption(data["shift"], line))
                                + "\n"
                            )

                    print(f"\nFile {file_name}(decoded).txt successfully created")

                    return

                else:
                    print("The file was not found")

                    continue

        case "manual":
            string: str = input("\nEnter the text: ")

            print(decode_full_shift_encryption(data["shift"], string))

            return
