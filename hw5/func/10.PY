def findall(str, ch):
 index = [] 
 count = 0
 for i in str:
   if i == ch:
        index.append(count)
   count += 1
 return index

string = input()
character =input() 
print(findall(string ,character))
