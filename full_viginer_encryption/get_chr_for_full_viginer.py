def get_chr_encode(first_list: list, list_of_key_word: list) -> str:

    second_step_list = []

    n = 0

    for i in first_list:

        try:

            if (i + list_of_key_word[n] + 31) < 127:

                second_step_list.append(i + list_of_key_word[n])

                n += 1

            elif (i + list_of_key_word[n] + 31) > 126:

                second_step_list.append(i + list_of_key_word[n] - 95)

                n += 1

        except IndexError:

            n = 0

            if (i + list_of_key_word[n] + 31) < 127:

                second_step_list.append(i + list_of_key_word[n])

                n += 1

            elif (i + list_of_key_word[n] + 31) > 126:

                second_step_list.append(i + list_of_key_word[n] - 95)

                n += 1

    return ''.join([chr(x + 31) for x in second_step_list])


def get_chr_decode(first_list: list, list_of_key_word: list) -> str:

    second_step_list = []

    n = 0

    for i in first_list:

        try:

            if (i - list_of_key_word[n]) > 0:

                second_step_list.append(i - list_of_key_word[n])

                n += 1

            elif (i - list_of_key_word[n]) < 1:

                second_step_list.append(i - list_of_key_word[n] + 95)

                n += 1

        except IndexError:

            n = 0

            if (i - list_of_key_word[n]) > 0:

                second_step_list.append(i - list_of_key_word[n])

                n += 1

            elif (i - list_of_key_word[n]) < 1:

                second_step_list.append(i - list_of_key_word[n] + 95)

                n += 1

    return ''.join([chr(x + 31) for x in second_step_list])
