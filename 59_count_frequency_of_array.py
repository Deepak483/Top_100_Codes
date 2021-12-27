# size_array = int(input("Enter the size of array: "))
# arr = []
# print("Enter the elements in array: ")
# for i in range(size_array):
#     arr.append(int(input()))

# # initializing empty list for counting
# empty_arr = list(dict.fromkeys(arr))
# for elements in empty_arr:
#     print(f"{elements} occur {arr.count(elements)} times")

size_array = int(input("Enter the size of array: "))
arr = []
for i in range(size_array):
    arr.append(int(input()))

element_arr = list(dict.fromkeys(arr))
# print(element_arr)
for x in element_arr:
    print(f"{x} occurs {arr.count(x)} time(s)")
