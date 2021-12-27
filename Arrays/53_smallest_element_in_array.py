# smallest element in array
arr_size = int(input("Enter the size of array"))
arr = []
for i in range(1, arr_size+1):
    value = int(input())
    arr.append(value)

print(f"smallest element in array is ", min(arr))
