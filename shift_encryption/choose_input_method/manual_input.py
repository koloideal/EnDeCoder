from shift_encryption.shift_encryption import (
    encode_shift_encryption,
    decode_shift_encryption,
)


def helper_encode_manual_input() -> str:
    while True:
        save_register: str = input("\nKeep the register?(0 - no, 1 - yes): ")

        if save_register not in ["0", "1"]:
            print("The input data can only be 0 or 1")

            continue

        else:
            break

    string: str = input("\nEnter the text: ")

    while True:
        try:
            shift: int = int(input("\nEnter the shift: "))

            if not 0 < shift < 27:
                raise TypeError

        except (TypeError, ValueError):
            print(
                'The data type of the "shift" argument can only be an integer in interval [1; 26]'
            )

            continue

        else:
            return encode_shift_encryption(shift, string, bool(int(save_register)))


def helper_decode_manual_input() -> str:
    while True:
        save_register: str = input("\nKeep the register?(0 - no, 1 - yes): ")

        if save_register not in ["0", "1"]:
            print("The input data can only be 0 or 1")

            continue

        else:
            break

    string: str = input("\nEnter the text: ")

    while True:
        try:
            shift: int = int(input("\nEnter the shift: "))

            if not 0 < shift < 27:
                raise TypeError

        except (TypeError, ValueError):
            print(
                'The data type of the "shift" argument can only be an integer in interval [1; 26]'
            )

            continue

        else:
            return decode_shift_encryption(shift, string, bool(int(save_register)))
