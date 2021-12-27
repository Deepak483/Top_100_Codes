size = int(input("enter size: "))
array = []
for i in range(size):
    array.append(int(input()))

array.sort()
print("Ascending order of array: ")
print(array)

print("Dscending order of array: ")
array.sort(reverse=True)
print(array)
