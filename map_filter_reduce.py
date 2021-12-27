from array import *

value = array('i', [])
n = int(input("Enter how many values you want to insert: "))
for i in range(n):
    x = int(input("Enter the next values:"))
    value.append(x)

_value = int(input("Number you want to search: "))
index = 0
for e in value:
    if e == _value:
        print(index)

    index += 1
