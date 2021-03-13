import time
import random
import string
import sys
x=100_000
sys.setrecursionlimit(x)

#                           Sorting

#   Bubble Sort
def BubbleSort (L):
    k = True
    n = len(L)

    for i in range(n-1):
        k = False

        for j in range(n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
                k = True

        if k == False:
            break;


#   Count Sort
def CountSort (L):
    M = max(L)
    n = len(L)
    fr = [0] * (M+1)

    for i in range(n):
        fr[L[i]] += 1

    j = 0
    for i in range(M+1):
        while fr[i] != 0:
            L[j] = i
            j +=1
            fr[i] -=1


#  Radix Sort
def Radix_digit(L, n, k):
    fr = [0] * 10

    for i in range(n):
        fr[(L[i] // k) % 10] += 1

    for i in range(1, 10):
        fr[i] += fr[i - 1]

    aux = [0] * n
    for i in range(n - 1, -1, -1):
        aux[fr[(L[i] // k) % 10] - 1] = L[i]
        fr[(L[i] // k) % 10] -= 1

    for i in range(n):
        L[i] = aux[i]


def Radix_word(L, n, k):
    aux = [0] * n
    fr = [0] * 52

    for item in L:
        index = min(len(item) - 1, k)
        letter = ord(item[-(index + 1)]) - 65
        if letter > 25:
            letter -= 6
        fr[letter] += 1

    for i in range(51):
        fr[i + 1] += fr[i]

    for i in range(n - 1, -1, -1):
        item = L[i]
        index = min(len(item) - 1, k)
        letter = ord(item[-(index + 1)]) - 65
        if letter > 25:
            letter -= 6
        aux[fr[letter] - 1] = item
        fr[letter] -= 1

    return aux


def RadixSort(L):
    n = len(L)

    if type(L[0]) == type('test'):
        M = len(L[0])
        for i in range(1, len(L)):
            if M < len(L[i]):
                M = len(L[i])

        for k in range(M):
            aux = Radix_word(L, n, k)

        for i in range(len(aux)):
            L[i] = aux[i]
    else:
        M = max(L)
        k = 1
        while M // k > 0:
            Radix_digit(L, n, k)
            k *= 10


#   Merge Sort
def MergeSort (L):
    if len(L) > 1:
        m = len(L) // 2
        Lf = L[:m]
        Rt = L[m:]

        MergeSort(Lf)
        MergeSort(Rt)

        i = j = k = 0

        while i < len(Lf) and j < len(Rt):
            if Lf[i] < Rt[j]:
                L[k] = Lf[i]
                i += 1
            else:
                L[k] = Rt[j]
                j += 1
            k += 1

        while i < len(Lf):
            L[k] = Lf[i]
            i += 1
            k += 1

        while j < len(Rt):
            L[k] = Rt[j]
            j += 1
            k += 1


#   Quick Sort
def Partition(L, l, r):
    i = (l - 1)
    p = random.randint(l, r)
    pivot = L[p]

    for j in range(l, r):
        if L[j] <= pivot:
            i = i + 1
            L[i], L[j] = L[j], L[i]

    L[i + 1], L[r] = L[r], L[i + 1]
    return (i + 1)


def QuickSort(L, l, r):
    if len(L) == 1:
        return L
    if l < r:
        p = Partition(L, l, r)
        QuickSort(L, l, p - 1)
        QuickSort(L, p + 1, r)


#   Random lists
def Random_str (n):
    letters = string.ascii_letters

    L = []
    for i in range(n):
        x = random.randint(2,20)
        y =  ''.join(random.choice(letters) for i in range(x))
        L.append(y)

    return L


def Random_int (n, sz):
    # n = lungimea listei
    # sz = lungimea numarului
    L = []
    for i in range(0, n):
        x = random.randint(0, sz)
        L.append(x)

    return L


def Random_float (n, sz):
    # n = lungimea listei
    # sz = lungimea int(numar)
    L = []
    for i in range(0, n):
        x = random.randint(1, sz)
        y = random.randint(0,99)
        z = float(x + (y / 100))
        L.append(z)

    return L


#   Time test
def Timer (l, p):

    L = l.copy()
    start = time.time()
    L.sort()
    stop = time.time()
    print("Python Sort: ", stop - start, " secunde")

    L = []
    L = l.copy()
    start = time.time()
    QuickSort(L, 0, len(L) - 1)
    stop = time.time()
    print("Quick Sort : ", stop - start, " secunde")

    L = []
    L = l.copy()
    start = time.time()
    BubbleSort(L)
    stop = time.time()
    print("Bubble Sort: ", stop - start, " secunde")

    if p == 0:
        L = []
        L = l.copy()
        start = time.time()
        CountSort(L)
        stop = time.time()
        print("Count Sort : ", stop - start, " secunde")

    if p != 1:
        L = []
        L = l.copy()
        start = time.time()
        RadixSort(L)
        stop = time.time()
        print("Radix Sort : ", stop - start, " secunde")

    L = []
    L = l.copy()
    start = time.time()
    MergeSort(L)
    stop = time.time()
    print("Merge Sort : ", stop - start, " secunde")


def Test ():
    print("Teste cu liste de lungime 10^6:")

    sz = 1_000
    n = 100_000
    i = random.randint(2, 3)
    for k in range(1, i+1):
        print("\nTestul "+ str(k)  + " pe numere naturale de dimensiuni mici [0:10^4]:")
        L = Random_int(n,sz)
        Timer(L, 0)

    i = random.randint(2, 3)
    for k in range(1, i+1):
        print("\nTestul " + str(k) + " pe numere reale de dimensiuni mici [0:10^4]:")
        L = Random_float(n, sz)
        Timer(L, 1)

    sz = 10_000_000
    i = random.randint(2, 3)
    for k in range(1, i+1):
        print("\nTestul " + str(k) + " pe numere naturale de dimensiuni mari [0:10^8]:")
        L = Random_int(n, sz)
        Timer(L, 0)

    i = random.randint(2, 3)
    for k in range(1, i+1):
        print("\nTestul " + str(k) + " pe numere reale de dimensiuni mari [0:10^8]:")
        L = Random_float(n, 1_000)
        Timer(L, 1)

    i = random.randint(2, 3)
    for k in range(1, i+1):
        print("\nTestul " + str(k) + " pe string-uri:")
        L = Random_str(n)
        Timer(L, 2)



def Test1():
                                        # Teste cu liste aproape ordonate
    print("Teste cu liste aproape ordonate:")

    n = 100_000
    i = random.randint(2, 3)
    for k in range(1, i+1):
        print("\nTestul " + str(k) + " pe numere naturale:")
        print("Len lista = ", n)
        L = [x for x in range(1,n+1)]
        for i in range(100):
            x = random.randint(0, n-1)
            y = random.randint(0, n-1)
            L[x], L[y] = L[y], L[x]
        Timer(L, 0)

                                        # Teste cu liste sortate descrescator
    print("\nTeste cu liste sortate descrescator:")

    i = random.randint(2, 3)
    for k in range(1, i + 1):
        print("\nTestul " + str(k) + " pe numere naturale:")
        print("Len lista = ", n)
        L = [x for x in range(n,-1,-1)]
        Timer(L, 0)

Test()
Test1()