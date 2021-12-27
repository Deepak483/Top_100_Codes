size_arr = int(input("Enter the size of element you want to enter: "))
arr = []
for i in range(size_arr):
    arr.append(int(input()))

print("Smallest element in array is ", min(arr))
print("Largest element in array ", max(arr))
