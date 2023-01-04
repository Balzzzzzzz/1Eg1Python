-> W sposób odejmowania

a,b = int(input()), int(input())
while a != b:
  if a > b : a = a - b
  if b > a : b = b - a
print(a)

    -> Pseudokod

    dopóki a =/ b wykonaj       (=/ oznacza różne)
      jeżeli a > b
         a = a - b
     jeżeli b > a
         b = b - a
    wypisz a

-> W sposób modulo

a,b = int(input()), int(input())
while b > 0:
  a,b = b , a % b
print(a)


    -> Pseudokod

    dopuki b > o wykonaj
       temp = a
        a = b
        b = temp mod(modulo) b
    wypisz a














