Zad 1
print("wpisz 3 liczby: ")
a = int(input())
b = int(input())
c = int(input())
if b - a == c - b: print("Ciąg jest arytmetyczny: " + a + b + c) 
if b / a == c / b: print("Ciąg jest geometryczny: " + a + b + c)
if a < b == b < c: print("Ciąg jest malejy: " + a + b + c)
if a > b == b > c: print("Ciąg jest rosnący: " + a + b + c)
  
 
Zad 2
suma = 0
for i in range(100,999):
 if i % 8 == 0 & i % 16 != 0:
   suma += i
print("Suma tych liczb: " + suma)

Zad 3



Zad 4
ilosc = 0
for i in range(10, 100):
    ilosc += 1
print(ilosc)

Zad 6
n = int(input())
suma = 0
i = 1
while n > 0:
    if i % 19:
        suma += i
        n -= 1
    i += 1
print(suma)


Zad 8
from math import pow
n = int(input())
suma = 0
for i in range(n):
    suma += (3*i+2) *  ((-1) ** i)
print(suma)
