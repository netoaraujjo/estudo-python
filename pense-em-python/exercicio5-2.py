def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print("No, that doesn't work.")


def read_input():
    a = int(input("Informe o valor de 'a': "))
    b = int(input("Informe o valor de 'b': "))
    c = int(input("Informe o valor de 'c': "))
    n = int(input("Informe o valor de 'n': "))

    check_fermat(a, b, c, n)


if __name__ == '__main__':
    read_input()
