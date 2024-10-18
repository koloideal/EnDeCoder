import helper
from atbash_encryption.atbash_encryption import (
    encode_atbash_encryption,
    decode_atbash_encryption,
)
from full_shift_encryption.full_shift_encryption import (
    encode_full_shift_encryption,
    decode_full_shift_encryption,
)
from full_viginer_encryption.full_viginer_encryption import (
    encode_full_viginer_encryption,
    decode_full_viginer_encryption,
)
from shift_encryption.shift_encryption import (
    encode_shift_encryption,
    decode_shift_encryption,
)
from user_encryption.user_encryption import (
    encode_user_encryption,
    decode_user_encryption,
)
from viginer_encryption.viginer_encryption import (
    encode_viginer_encryption,
    decode_viginer_encryption,
)


name_func_to_func: dict = {
    "encode shift encryption": encode_shift_encryption,
    "decode shift encryption": decode_shift_encryption,
    "encode full shift encryption": encode_full_shift_encryption,
    "decode full shift encryption": decode_full_shift_encryption,
    "encode user encryption": encode_user_encryption,
    "decode user encryption": decode_user_encryption,
    "encode atbash encryption": encode_atbash_encryption,
    "decode atbash encryption": decode_atbash_encryption,
    "encode viginer encryption": encode_viginer_encryption,
    "decode viginer encryption": decode_viginer_encryption,
    "encode full viginer encryption": encode_full_viginer_encryption,
    "decode full viginer encryption": decode_full_viginer_encryption,
}

name_funcs: dict = {
    1: "encode shift encryption",
    2: "decode shift encryption",
    3: "encode full shift encryption",
    4: "decode full shift encryption",
    5: "encode user encryption",
    6: "decode user encryption",
    7: "encode atbash encryption",
    8: "decode atbash encryption",
    9: "encode viginer encryption",
    10: "decode viginer encryption",
    11: "encode full viginer encryption",
    12: "decode full viginer encryption",
}


def get_help() -> None:
    print(
        '\nSelect the function or enter "stop" to exit the menu, to get help on the operation of the encryption '
        "method, you must enter its serial number\n"
    )

    for k, i in enumerate(name_func_to_func.keys()):
        print(f"{k + 1}: {i}")

        if k % 2 != 0:
            print()

    while True:
        name_func: str = input('Enter a query or "stop": ')

        if name_func not in [str(x + 1) for x in range(12)] and name_func != "stop":
            print("Incorrect input\n")

            continue

        else:
            if name_func == "stop":
                print("\nReturn to the action selection mode\n")

                break

            else:
                int_name = int(name_func)

                print(f'\nDescription of the "{name_funcs[int_name]}" function\n')

                print(" ".join(name_func_to_func[name_funcs[int_name]].__doc__.split()))

                print()

                continue

    helper.helper()

    return
