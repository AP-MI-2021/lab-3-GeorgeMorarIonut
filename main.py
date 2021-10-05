def isPrime(x):
    """
    Determina daca un numar este prim.
    :param x: nr intreg
    :return: True daca numarul este prim sau False in caz contrar.
    """
    if x < 2:
        return False
    else:
        for i in range(2 , x // 2 + 1):
            if x % i == 0:
                return False
    return True


assert isPrime(13) is True
assert isPrime(1) is False
assert isPrime(2) is True


def get_longest_all_primes(lst: list[int]) -> list[int]:
    """
    Determina cea mai lunga subsecventa de numere prime.
    :param lst: o lista de numere.
    :return: cea mai lunga subsecventa de numere prime din lista data.
    """
    cont = 0
    contMax = 0

    for i in lst:
        if isPrime(i):
            cont = cont + 1
        else:
            if cont > contMax:
                contMax = cont
            cont = 0
    cont = 0
    for i in lst:
        if isPrime(i):
            cont = cont + 1
        else:
            if cont == contMax:
                for j in range(lst.index(i) - cont - 1, lst.index(i) - 1):
                    print(lst[j])
            cont = 0
    if contMax == 0:
        print("Nu exista numere prime in lista!")


def main():

    lst = [4, 2, 3, 6, 3, 5, 11, 7, 4]
    get_longest_all_primes(lst)

if __name__ == '__main__':
    main()

