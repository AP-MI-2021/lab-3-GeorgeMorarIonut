def citireLista ():
    l = []
    n = int(input("Dati numarul de elem din lista: "))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]= ")))
    return l


def isPrime(x):
    """
    Determina daca un numar este prim.
    :param x: nr intreg
    :return: True daca numarul este prim sau False in caz contrar.
    """
    if x < 2:
        return False
    else:
        for i in range(2, x // 2 + 1):
            if x % i == 0:
                return False
    return True

def testPrimeFunction():
    assert isPrime(13) is True
    assert isPrime(1) is False
    assert isPrime(2) is True


def noneArePrimes (l):
    """
    Determina daca toate numerele dintr-o lista sunt prime
    :param l: O lista de numere intregi
    :return: True daca toate numerele dintr-o lista sunt prime sau False, in caz contar.
    """
    for i in l:
        if isPrime(i):
            return False
    return True


def testNonePrimesFunction():
    assert noneArePrimes([]) is True
    assert noneArePrimes([1, 2, 3]) is False
    assert noneArePrimes([1, 4, 8, 9]) is True


def get_longest_all_not_primes(l):
    """
    Determina cea mai lunga subsecventa de numere neprime.
    :param l: O lista de numere intregi
    :return: Afiseaza cea mai lunga subsecventa de numere neprime dintr-o lista.
    """
    secvMax = []

    for i in range(len(l)):
        for j in range(i, len(l)):
            if noneArePrimes(l[i: j + 1]) and len(l[i: j + 1]) > len(secvMax):
                secvMax = l[i: j + 1]
    return secvMax


def testLongestNotPrimesFunction():
    assert get_longest_all_not_primes([]) == []
    assert get_longest_all_not_primes([1, 2, 3, 4, 6, 12, 14, 5, 7, 2, 8, 10, 26]) == [4, 6, 12, 14]
    assert get_longest_all_not_primes([2, 3, 5, 7]) == []


def numbersAverage(l):
    """
    Determina media aritmetica a  numerelor dintr-o lista.
    :param l: o lista de numere
    :return: Media aritmetica a numerelor din lista data.
    """
    sumNr = 0
    contNr = 0
    for i in l:
        sumNr = sumNr + i
        contNr = contNr + 1
    if contNr == 0:
        return 0
    return sumNr / contNr


def testNumbersAverage():
    assert numbersAverage([2, 7]) == 4.5
    assert numbersAverage([1, 4, 6, 5]) == 4
    assert numbersAverage([2, 2, 2, 2, 2, 2]) == 2


def get_longest_average_below(l, average):
    """
    Determina cea mai lunga subsecventa in care media numerelor este mai mica decat o valoare data.
    :param l: o lista de numere
    :param average: un numar intreg
    :return: o subsecventa din lista initiala
    """
    secvMax = []

    for i in range(len(l)):
        for j in range(i, len(l)):
            if numbersAverage(l[i: j+1]) < average and len(l[i: j+1]) > len(secvMax):
                secvMax = l[i: j+1]
    return secvMax


def test_get_longest_average_below():
    assert get_longest_average_below([], 12) == []
    assert get_longest_average_below([456, 3, 4, 5, 6, 765, 4, 5, 678, 78], 10) == [3, 4, 5, 6]
    assert get_longest_average_below([678, 4, 5, 678, 2, 4, 6, 9, 432, 456], 10) == [2, 4, 6, 9]


def powersOfK (l, k):
    """
    Determina daca intr-o lista de numere toate sunt puteri ale lui un numar dat k.
    :param l: o lista de numere
    :param k: un numar intreg
    :return:True daca toate numerele din lista sunt puteri ale lui k sau False in caz contrar.
    """
    for i in l:
        while i % k == 0:
            i = i // k
        if i != 1:
            return False
    return True


def testPowersOfK():
    assert powersOfK([], 2) is True
    assert powersOfK([2, 4, 8, 5, 25, 64, 128], 5) is False
    assert powersOfK([2, 4, 8, 64], 2) is True


def get_longest_powers_of_k(l, k):
    """
    Determina cea mai lunga subsecventa dintr-o lista de numere in care toate numerele sunt puteri ale lui k.
    :param l: o lista de numere
    :param k: un numar intreg
    :return: cea mai lunga subsecventa din lista data de numere in care toate numerele sunt puteri ale lui k
    """
    secvMax = []

    for i in range(len(l)):
        for j in range(i, len(l)):
            if powersOfK(l[i: j + 1], k) and len(l[i: j + 1]) > len(secvMax):
                secvMax = l[i: j + 1]
    return secvMax


def test_get_longest_powers_of_k():
    assert get_longest_powers_of_k([3, 2, 32, 8, 64, 16, 32, 6, 9, 12], 2) == [2, 32, 8, 64, 16, 32]
    assert get_longest_powers_of_k([], 5) == []
    assert get_longest_powers_of_k([3, 12, 5, 17, 18], 2) == []


def main():

    testPrimeFunction()
    testNonePrimesFunction()
    testLongestNotPrimesFunction()
    testNumbersAverage()
    test_get_longest_average_below()
    testPowersOfK()
    test_get_longest_powers_of_k()


    l = []

    while True:
        print("1. Citire date")
        print("2. Determinati cea mai lunga subsecventa de numere neprime dintr-o lista")
        print("3. Determinati cea mai lunga subsecventa in care media numerelor este mai mica decat o valoare data.")
        print("4. Determinati cea mai lunga subsecventa in care toate numerele sunt puteri ale lui k.")
        print("5. Iesire")

        optiune = input("Selectati optiune: ")

        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print(get_longest_all_not_primes(l))
        elif optiune == "3":
            average = int(input("Introduceti valoare average: "))
            print(get_longest_average_below(l, average))
        elif optiune == "4":
            k = int(input("Introduceti valoare k: "))
            print(get_longest_powers_of_k(l, k))
        elif optiune == "5":
            break
        else:
            print("Optiune gresita! Selectati alta optiune.")


if __name__ == '__main__':
    main()

