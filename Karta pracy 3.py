1.tablica mnożenia:
  for i in range(1,11):
   for j in range(1,11):
    print(i*j , "\t", end= "")
   print()
  
  
 2.hoinki
1
n=int(input())
for i in range(n):
  for j in range(i+1):
    print("*", end= "")
  print()

2
n=int(input())
for i in range(n):
 for j in range(n-i-1):
  print(" ", end="")
  for k in range(n-i-1, n):
    print("*", end= "")
  print()



































