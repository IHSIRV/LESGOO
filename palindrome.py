
def check_palindrome(*args):
    """
    A function to check for palindrome sequences
        Inputs: Iterables (strings, lists)
        More specifically hashable objects on which str() is semantically applicable

        Output: A dictionary of (object, bool)
        More specifically bool1 = True if object1 was a palindrome
    """

    temp_dict_return = {}

    def single_palindrome(temp_input):
        temp_bool_return = False
        temp_str = str(temp_input)

        for temp_index in range(0, len(temp_str)):
            if temp_str[temp_index] == temp_str[-1 * temp_index - 1]:
                temp_bool_return = True
            else:
                temp_bool_return = False
                return {temp_input: False}

        return {temp_input: temp_bool_return}

    for element in args:
        single_check = single_palindrome(element)

        temp_dict_return.update(single_check)

    return temp_dict_return


# Calling the function
int_example = 10.1  # using str( int ) to convert it to iterable, could not figure out a general way in n-base, eg 10.1
str_example = '02022020'  # works perfectly
tup_example = (1, 2, '3', 2, 1)  # we couldn't figure how to make them work


print(check_palindrome(str_example, int_example))
print("This doesn't work as intended", check_palindrome(tup_example), 'see?')
