1.tablica mnożenia:
  for i in range(1,11):
   for j in range(1,11):
    print(i*j , "\t", end= "")
   print()
  
  
 2.hoinki
A)
n=int(input())
for i in range(n):
  for j in range(i+1):
    print("*", end= "")
  print()

B)
n=int(input())
for i in range(n):
 for j in range(n-i-1):
  print(" ", end="")
  for k in range(n-i-1, n):
    print("*", end= "")
  print()
  
  Zad 1
  
         n = int(input())

for i in range(n):
   print("|*, end="")
         print()
  Zad 2
         
         n = int(input())

for i in range(1, n+1):
  print("*" * i, end="")
  if i % 2:
    print("||", end="")
  else:
    print("--", end="")
         print()
         
 Zad 3
  
n = int(input())
for i in range(1,n+1):
    print("*", end="")
    if i % 2 == 1:
        print("|" * i, end="")
    else:
        print("-" * i, end="")
print()
    
Zad 4
  

         
         
Zad 5         

n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==n//2+1:
            print("*", end="")
        elif i==n//2+1:
            print("-", end="")
        else:
            print(" ", end="")
    print()
    if 5:
        if 6:
            if 6:
                pass
            else:
                pass
        else:
            if 6:
                pass
         

Zad 6         

n = int(input())
for i in range(n):
    for j in range(n+1):
        if j==i and not j==n//2:
            print("*", end="")
        elif j==n-i:
            print("?", end="")
        print(" ", end="")
    print()

         
           zad 7
n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or i == n or j == 1 or j == n or (i==n//2+1 and j ==n//2+1):
            print("*", end="")
        else:
            print(" ", end="")
    print()






























