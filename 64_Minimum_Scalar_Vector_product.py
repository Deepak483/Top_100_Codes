l1_array = list(map(int, input("Enter the elements in array1: ").split()))
l2_array = list(map(int, input("Enter the elements in array2: ").split()))

sum = 0
l1_array.sort()  # sort in ascending order
l2_array.sort(reverse=True)  # sort in descending order

for i in range(0, len(l1_array)):
    for j in range(0, len(l2_array)):
        if (i == j):
            sum = sum + l1_array[i]*l2_array[j]

print('Minimum scalar product of two arrays is', end='')
print(sum)
