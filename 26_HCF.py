num1 = int(input())
num2 = int(input())
arr = []

if num1 > num2:
    smaller = num2
else:
    smaller = num1

for i in range(1, smaller+1):
    if (num1 % i == 0) and (num2 % i == 0):
        arr.append(i)

print(f"Hcf of {num1} and {num2} is {max(arr)}")
print("Hcf of num1 and num2 is ",max(arr))
