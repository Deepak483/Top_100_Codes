size_arr = int(input("Enter the size of element you want to enter: "))
arr = []
sum = 0
for i in range(size_arr):
    arr.append(int(input()))
    sum += arr[i]

# we can also use inbuilt sum function
print(f"sum of element in array is {sum}")
