def do_twice(f, txt):
    f(txt)
    f(txt)


def do_four(f, txt):
    do_twice(f, txt)
    do_twice(f, txt)


def print_spam(txt):
    print(txt)


do_four(print_spam, 'spam')