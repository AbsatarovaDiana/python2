import random
def rand(x):
    num = random.randint(10**(x-1),(10**x)-1)
    return num
    
number= int(input())
print(rand(number))