num = int(input("Enter the number: "))

arr = []
prime_number = []
for i in range(2, num):
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        arr.append(i)

flag = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if (arr[i]+arr[j] == num):
            flag = 1
            # print(f"{str(arr[i])} and {str(arr[j])} when added gives {num}")
            prime_number.append(arr[i])
            prime_number.append(arr[j])
            break

prime_number.sort()
print("This prime numbers can given addition of numbers ", prime_number)
if(flag == 0):
    print(f"No prime numbers are added to given sum {num}")
