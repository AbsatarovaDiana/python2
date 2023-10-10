def near_to_max(l, n):
   max = 0
   for i in l:             
      if i < n and max < i :   
        max = i  
   return max     
L = [1,6,3,9,11]              
n = 8
print("Result is :",near_to_max(L, n)) 
             