

def check_anagram(temp_str_1: str, temp_str_2: str):
    """
    CHECK_ANAGRAM(string1, string2) --> Bool

    returns True only if the striped(' ') strings
    have same letters.

    CASE INSENSITIVE
    """
    bool_return = False

    temp_str_1 = (temp_str_1.strip(' ')).lower()
    temp_str_2 = (temp_str_2.strip(' ')).lower()

    if len(temp_str_1) == len(temp_str_2):
        # Possibility of Anagrams

        list_letters_1 = list(temp_str_1)
        list_letters_2 = list(temp_str_2)

        int_running_index = 0
        for int_first_index in range(0, len(list_letters_1)):

            str_letter = list_letters_1[int_running_index]

            if str_letter in list_letters_2:
                list_letters_1.remove(str_letter)
                list_letters_2.remove(str_letter)
            else:
                int_running_index = int_running_index + 1

        if list_letters_1 == list_letters_2 == []:
            bool_return = True
            return bool_return
        else:
            return bool_return

    return bool_return


str_1 = '     Heart'
str_2 = 'Earth'


print(check_anagram(str_2, str_1))
