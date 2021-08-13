import turtle

# defining a method and default value


def add_list_numbers(list_name=[1, 2]):
    total = 0
    for number in list_name:
        total = total + number
    return total

# palindrome checker


def is_palindrome(orig_string):
    letters_list = list(orig_string)
    letters_list.reverse()
    rev_string = ''.join(letters_list)
    return orig_string == rev_string


def main():
    some_list = [2, 4, 4]
    print(add_list_numbers(some_list))
    print("hello")

    print(is_palindrome("tacocat"))


if __name__ == "__main__":
    main()
