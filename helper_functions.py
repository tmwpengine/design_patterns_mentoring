from random import randint, choice
import string


def get_random_number_less_than_ten():
    return randint(0, 10)


def get_random_letter():
    return choice(string.ascii_letters)


def remove_first_character(s):
    return s[1:]


def add_five(x):
    try:
        return x + 5
    except TypeError:
        print("Can only add int 5 to another int")
        raise


def add_five_to_random_int_less_than_ten():
    return 5 + get_random_number_less_than_ten()

