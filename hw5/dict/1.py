dict = {
    'Albert Einstein' : '03/14/1879' ,
    "Benjamin Franklin" : '01/17/1706' ,
    "Ada Lovelace" : '12/10/1815'
}
print("Welcome to the birthday dictionary. We know the birthdays of:" )
print(dict.keys())
v = input("Whos birthday do you want to look up?", )
for i in dict:
 if dict[i] == dict[v]:
  print(f"{v}'s birthday is {dict[i]}.")




