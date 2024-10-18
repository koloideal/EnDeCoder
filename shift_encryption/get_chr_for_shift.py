def get_chr_encode(shift: int, ords: int) -> str:
    dict_of_chr: dict = {}

    for i in range(97, 123):
        dict_of_chr[i - 96]: str = chr(i)

    return dict_of_chr.get(
        (ords + shift) if (ords + shift) <= 26 else ((ords + shift) - 26)
    )


def get_chr_decode(shift: int, ords: int) -> str:
    dict_of_chr: dict = {}

    for i in range(97, 123):
        dict_of_chr[i - 96]: str = chr(i)

    return dict_of_chr.get(
        (ords - shift) if (ords - shift) > 0 else ((ords - shift) + 26)
    )
