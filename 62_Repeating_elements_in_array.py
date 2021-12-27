# firstly method1 by using set
# size = int(input("enter the length of array: "))
# arr = []

# # taking the input array
# for i in range(size):
#     arr.append(int(input()))

# # condition iterating over set()
# print("this elements are repeating :")
# for i in set(arr):
#     if arr.count(i) > 1:
#         print(f"{i} ", end=' ')

elements_list = list(map(int, input("Enter the elements:  ").split()))
another_arr = []

for i in elements_list:
    if (elements_list.count(i) > 1 and i not in another_arr):
        another_arr.append(i)

# repeating elements in array
print("Repeating elements in array is ", another_arr)
