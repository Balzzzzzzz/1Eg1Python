# 1 (easy) Sprawdź czy suma dwóch wpisanych przez użytkownika jest liczbą parzystą.
# Wejście: a, b
# Wyjście: TAK / NIE

a = int(input())
b = int(input())
  if (a+b) % 2 == 0:
      print("suma tych liczb jest parzystą")
  else:
      print("suma tych liczb jest nie parzystą")
  

# 2. (easy) Sprawdź, czy średnia arytmetyczna dwóch wpisanych liczb jest wieksza od jej średniej geometrycz-nej.
# Wejście: a,g
# Wyjście: TAK / NIE
  
  a = int(input())
g = int(input())
 if (a+g) / 2 > ( a*g ) ** 0.5:
    print("Tak, jest większa")
 else:
    print("Nie, nie jest większą")

  
#   3. (easy) Użytkownik podaje 3 liczby całkowite. Sprawdź czy dokładnie dwie z nich są sobie równe.
#   Wejście: k,l,m
#     Wyjście: TAK / NIE (wraz z podaniem tych dwóch równych o ile są takowe)
      k = int(input())
l = int(input())
m = int(input())
if (k==l and k==m and m==l):
  print("TAK")
else:
  print("NIE")

  
  
#       4. (medium) Niech użytkownik wprowadzi 4 różne liczby całkowite. 
#       Napisz program, który sprawdzi, któraz tych liczb jest najmniejsza.
#       Wejście: a,b,c,d
#         Wyjście: najmniejsza z nich
          
  
  
  
  
#           5. (medium) Sprawdź czy trzy wprowadzone przez użytkownika liczby spełniają nierówność trójkąta.
#           Wejście: a, b, c
#             Wyjście: TAK / NIE





#               6. (medium) Niech z trzech wprowadzonych przez użytkwnika liczbach da się zbudować trójąt. 
#               Sprawdź czyten trójką jest ostrokątny, prostokątny czy rozwartokątny.
#               Wejście: a, b, c
#                 Wyjście: ostro-, prosto-, rozwarto-kątny
