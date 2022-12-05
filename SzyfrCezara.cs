#Szyfr Cezara


# # Funkcja ord() - zwraca kod ascii podanego znaku 

# print(ord("A"))
# print(ord("B"))
# print(ord("Z"))


# # Funkcja chr() - zwraca znak dla podanego kodu ascii

# print(chr(65))
# print(chr(66))
# print(chr(90))


# Połączenie w całość:

# print(chr(ord("C")))
# print(chr(ord("C") + 2))

#1. Wypisz alfabet A-Z za pomocą pętli for

# for i in range(65,91):
#   print(chr(i), end=" ")


# Jak z napisu wyjąć literki:

# napis = "POLSKA"
# print(len(napis))
# print(napis[0])
# print(napis[1])
# print(napis[2])

# 2. Wypisz litery napisu w pętli

# napis = input()
# for i in range(len(napis)):
#   print(napis[i])


# 3. Wypisz kody ascii liter napisu

# napis = input()
# for i in range(len(napis)):
#   print(ord(napis[i]))


# 4. Zaszyfruj napis w kodzie Cezara o kluczu = 3

# napis = input()
# for i in range(len(napis)):
#   print(chr(ord(napis[i]) + 3))


napis = input()
szyfr = ""
for i in range(len(napis)):
  szyfr = szyfr + chr(65 + (ord(napis[i]) - 65 + 5) % 26)
print(napis, szyfr)





