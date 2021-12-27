# [23,2,3,4,23,7,7]
# distinct element from array is 23,2,3,4,7
# therefore count of it is 5

# arr_len = int(input("Enter the length of array: "))
# array = []

# for i in range(arr_len):
#     array.append(int(input()))

# array_set = set(array)
# print(f"Distinct element in array: "+array_set.count())

arr = list(map(int, input("Enter Array element in array: ").split()))
x = list(dict.fromkeys(arr))  # to remove element in array
print("Element of array ", *arr)
print("Element of array without duplicates : ", *x)
print("count of distinct element in array ", len(x))
