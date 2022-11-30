NWW - Najmniejsza Wspulna Wielokrotna

NWW ( 8 , 6 ) = 24
while a % b == 0 : a = a + a
  
 8 * 6 = 2 * 24
a * b = NWD(a , b) * NWW(a , b)


przez odejmowanie:
  
  a,b = int(input()), int(input())
while a != b :
  if a > b : a = a - b
  if b > a : b = b - a
print(a)


przez modulo:
  
  a,b = map(int, input().split())
iloczyn = a * b
while b > 0 :
  a,b = b, a % b
nwd  = a
print(a=iloczyn // nwd)















