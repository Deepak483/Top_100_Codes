arr_size = int(input("enter the size of array: "))
arr1 = []
arr2 = []
for i in range(0, arr_size//2):
    a = int(input())
    arr1.append(a)
    arr1.sort()


for i in range((arr_size)//2, arr_size):
    b = int(input())
    arr2.append(b)
    arr2.sort(reverse=True)

print(arr1+arr2)
