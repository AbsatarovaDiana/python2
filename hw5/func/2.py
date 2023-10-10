def add_excitement(list_of_str):
    for i in range(len(list_of_str)):
          list_of_str[i] = list_of_str[i]+"!"
    return list_of_str

def add_excitement2(list_of_str):
    for i in range(len(list_of_str)):
          list_of_str[i] = list_of_str[i]+"!"
    newlist = []
    newlist = [n for n in list_of_str]
    return newlist

            
str = input("Enter strings separated by comma:", )
list = str.split(',')
print(add_excitement(list))
print(add_excitement2(list))
