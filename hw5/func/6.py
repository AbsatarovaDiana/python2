import math as m
def binom(n, k):
    if n>k:
     return m.factorial(n)/(m.factorial(k)*m.factorial(n-k))
    else:
       return "n less than k"
n= int(input())
k = int(input())
print(binom(n,k))