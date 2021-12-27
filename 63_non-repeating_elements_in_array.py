# here i am using set for finding the non repeating elements
array_ele = list(map(int, input("Enter the elements: ").split()))

print("this are non-repeating elements in array: ")
for i in set(array_ele):
    if array_ele.count(i) == 1:
        print(f"{i} ", end=' ')
