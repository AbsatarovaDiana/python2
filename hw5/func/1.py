def myFunc(m , n):
  
  for i in range(n):
    for j in range(m):
        print('*', end = ' ')

    print(" ")

x = int(input())
y = int(input())

myFunc(x, y)