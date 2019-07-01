from helper_functions import remove_first_character, get_random_letter

# Key Python concept in understanding Decorators


# A function can be assigned
def print_some_text(s):
    print(s)

f1 = print_some_text

f1("Hellooooo")


# A function can be passed into a function as an argument
def add_two(x):
    print(x + 2)


def function_wrapper(func):
    func(10)

function_wrapper(add_two)


# A function can live inside another function
def add_one(x):
    def add_another_one(x):
        print(x + 1)

    y = x + 1

    add_another_one(y)

add_one(5)


# A function can return another function
def return_function_that_adds_five():
    def add_five(i):
        print(i + 5)

    return add_five

new_func = return_function_that_adds_five()
print(new_func)
print(type(new_func))
new_func(10)


# A nested function has access to enclosing variables scope
def demo_nested_function_accessing_parent_scope(s):
    def nested_function():
        print(s)

    nested_function()

demo_nested_function_accessing_parent_scope("some stuff")


# Creating a decorator that extends another objects functionality by converting a string to uppercase (The old way)

# first decorating function
def add_random_letter(func):
    # import pdb; pdb.set_trace()
    def wrapper():
        original_value = func()
        decorated_value = f'{original_value} {get_random_letter()}'
        return decorated_value

    return wrapper


# a function to decorate
def return_some_string():
    return "abc"

decorated_response = add_random_letter(return_some_string)
print(decorated_response())


# (The new way)
@add_random_letter
def return_some_other_string():
    return "def"

print(return_some_other_string())


# Applying more than one decorator
# second decorating function
def remove_char(func):
    def wrapper():
        original_value = func()
        decorated_value = remove_first_character(original_value)
        return decorated_value

    return wrapper


@add_random_letter
@remove_char
def return_some_other_string():
    return "def"

print(return_some_other_string())


# decorating functions that accepts arguments

def to_upper(func):
    def wrapper(t):
        decorated_value = func(t).upper()
        return decorated_value

    return wrapper


@to_upper
def print_your_string(s):
    return s

print(print_your_string("hello"))

