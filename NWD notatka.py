-> W sposób odejmowania

a,b = int(input()), int(input())
while a != b:
  if a > b : a = a - b
  if b > a : b = b - a
print(a)


//MODULO = ???

19 % 7 = 2 5/7 = 5

19 % 18 = 1

19 % 19 = 0

19 % 20 = 19

-> W sposób modulo
a,b = int(input()), int(input())
while b > 0:
  a,b = b , a % b
print(a)

