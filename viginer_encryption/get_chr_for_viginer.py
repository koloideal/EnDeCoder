def get_chr_encode(first_list: list, list_of_key_word: list, save_register: bool, string: str) -> str:

    second_step_list = []

    n = 0

    for i in first_list:

        try:

            if isinstance(i, str):

                second_step_list.append(i)

                continue

            elif (i + list_of_key_word[n]) < 27:

                second_step_list.append(i + list_of_key_word[n])

                n += 1

                continue

            elif (i + list_of_key_word[n]) > 26:

                second_step_list.append(i + list_of_key_word[n] - 26)

                n += 1

                continue

        except IndexError:

            n = 0

            if isinstance(i, str):

                second_step_list.append(i)

                continue

            elif (i + list_of_key_word[n]) < 27:

                second_step_list.append(i + list_of_key_word[n])

                n += 1

                continue

            elif (i + list_of_key_word[n]) > 26:

                second_step_list.append(i + list_of_key_word[n] - 26)

                n += 1

                continue

    third_step_list = [chr(x + 96) if isinstance(x, int) else x for x in second_step_list]

    if save_register:

        fourth_step_list = []

        for k, i in enumerate(third_step_list):

            if string[k].isupper():

                fourth_step_list.append(i.upper())

            else:

                fourth_step_list.append(i)

        return ''.join(fourth_step_list)

    else:

        return ''.join(third_step_list)


def get_chr_decode(first_list: list, list_of_key_word: list, save_register: bool, string: str) -> str:

    second_step_list = []

    n = 0

    for i in first_list:

        try:

            if isinstance(i, str):

                second_step_list.append(i)

                continue

            elif (i - list_of_key_word[n]) > 0:

                second_step_list.append(i - list_of_key_word[n])

                n += 1

                continue

            elif (i - list_of_key_word[n]) <= 0:

                second_step_list.append(i - list_of_key_word[n] + 26)

                n += 1

                continue

        except IndexError:

            n = 0

            if isinstance(i, str):

                second_step_list.append(i)

                continue

            elif (i - list_of_key_word[n]) > 0:

                second_step_list.append(i - list_of_key_word[n])

                n += 1

                continue

            elif (i - list_of_key_word[n]) <= 0:

                second_step_list.append(i - list_of_key_word[n] + 26)

                n += 1

                continue

    third_step_list = [chr(x + 96) if isinstance(x, int) else x for x in second_step_list]

    if save_register:

        fourth_step_list = []

        for k, i in enumerate(third_step_list):

            if string[k].isupper():

                fourth_step_list.append(i.upper())

            else:

                fourth_step_list.append(i)

        return ''.join(fourth_step_list)

    else:

        return ''.join(third_step_list)
