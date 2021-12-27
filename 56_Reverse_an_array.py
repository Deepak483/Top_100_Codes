size_arr = int(input("Enter the size of element you want to enter: "))
arr = []
for i in range(size_arr):
    arr.append(int(input()))

print()
for i in reversed(range(size_arr)):
    print(arr[i])
