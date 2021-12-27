# maximum product of subarray
result = 1
n = int(input("Enter the length of array: "))
arr = []

print("Enter element of array: ")
print("Hello world")
for i in range(n):
    arr.append(int(input()))

for i in range(n):
    product = 1

    for j in range(i, n):
        result = max(result, product)
        product = product * arr[j]
    result = max(product, result)
print("Minimum number :")
print("Maximum product of subarray is ,", result)
