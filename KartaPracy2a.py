# zad 1
a, b = map(int, input("Wpisz dwie liczby przez spację: ").split())
if (a + b) % 2 == 0:
    print("suma jest liczbą parzystą")
else:
    print("suma nie jest liczbą parzystą")

# zad 2
a, g = map(int, input("podaj dwie dowolne liczby prez spację: ").split())
if (a+g)/2 > (a*g) ** 0.5:
    print("średnia arytmetyczna dwóch wpisanych liczb jest wieksza")
else:
    print("średnia arytmetyczna nie jest większa od średniej geomentrycznej")

# zad 3
k, l, m = map(int, input("Podaj 3 liczby całkowite: ").split())
if k == l == m:
    print("Wszystkie liczby są równe:", k)
if (k == l) and not(k == l == m):
    print("k = l =", k)
if (k == m) and not(k == l == m):
    print("k = m =", k)
if (l == m) and not(k == l == m):
    print("l = m =", l)

zad 4
print("Najmniejsza z podanych liczb:",min(map(int, input("Podaj 4 dowolne liczny całkowite: ").split())))

a, b, c, d = map(int, input("podaj 4 dowolne liczny całkowite: ").split())
min = a
if min>b:
    min=b
if min>c:
    min=c
if min>d:
    min=d
print(min)

# zad 5
a, b, c = map(int, input("Podaj 3 długości boków trójkąta: ").split())
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Tak, spełniają")
else:
    print("Nie, nie spełniają")

# zad 6
a, b, c = map(int, input("Wprowadź długości trzech boków trójkąta: ").split())
if (a+b>c) and (b+c>a) and (a+c>b):
    max = a
    b1 = b
    b2 = c
    if max < b:
        max = b
        b1 = a
    if max < c:
        max = c
        b1 = a
        b2 = b
    if (max**2) == (b1**2 + b2**2):
        print("Trójkąt prostokątny")
    if (max**2) < (b1**2 + b2**2):
        print("trójkąt ostrokątny")
    if (max**2) > (b1**2 + b2**2):
        print("trójkąt rozwartokątny")
else:
    print("To nie jest trójkąt")
