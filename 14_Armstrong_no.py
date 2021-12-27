# num = int(input("Enter the Number :"))
# order = len(str(num))
# temp = num
# sum = 0
# while temp > 0:
#     digit = temp % 10
#     sum += digit**3
#     temp = temp // 10

# if num == sum:
#     print(f"{num} is Armstrong Number")
# else:
#     print(f"{num} is Not Armstrong Number")

# method 2
import math
num = int(input("Enter the Number :"))
value = [int(d) for d in str(num)]
sum = 0
for i in range(0, len(value)):
    sum = sum + math.pow(value[i], len(value))

if sum == num:
    print(f"{num} is Armstrong Number")
else:
    print(f"{num} is Not Armstrong Number")
