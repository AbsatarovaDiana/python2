def digit_root(num):
    n=str(num)
    if len(n)<=1:
        return num

    else:
        sum=0
        for i in range(len(n) ):
            sum+=int(n[i] )

        return digit_root(sum)
x = int(input())
print(digit_root(x))