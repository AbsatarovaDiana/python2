def sum_n(n):

    sum_of_digits=0
    while n >1:

      x = n%10
      sum_of_digits += x
      n = n//10
    return sum_of_digits
num = int(input())
print(sum_n(num))
