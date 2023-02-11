def is_triangle(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        print('No')
    else:
        print('Yes')


def read_input():
    a = int(input("Digite o valor de 'a': "))
    b = int(input("Digite o valor de 'b': "))
    c = int(input("Digite o valor de 'c': "))

    is_triangle(a, b, c)


if __name__ == '__main__':
    read_input()
