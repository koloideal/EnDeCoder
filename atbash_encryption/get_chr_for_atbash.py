def get_chr(list_of_ords: list) -> list:

    dict_of_chr: dict = {}

    for i in range(97, 123):

        dict_of_chr[i - 96] = chr(i)

    return [dict_of_chr[x] if isinstance(x, int) else x for x in list_of_ords]
