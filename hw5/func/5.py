def first_diff(s1, s2):
    if len(s1)==len(s2):
     for i in range(len(s1)):
        if s1[i]!=s2[i]:
            return i
     else:
         return -1
    else:
            return -1
str1= input()
str2= input()
print(first_diff(str1, str2))

    