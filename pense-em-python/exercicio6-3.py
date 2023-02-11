def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    if len(word) == 0:
        return False
    elif len(word) == 1:
        return True
    elif len(word) == 2:
        return first(word) == last(word)
    else:
        return first(word) == first(word) and is_palindrome(middle(word))


if __name__ == '__main__':
    print(is_palindrome('neto'))