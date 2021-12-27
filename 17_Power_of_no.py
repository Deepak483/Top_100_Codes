# base = int(input("Enter Base Number: "))
# expo = int(input("Enter Exponent: "))

# temp = 1
# for i in range(expo):
#     temp = temp * base

# print(temp)
import math
base = int(input("Enter Base Number: "))
expo = int(input("Enter Exponent: "))

print(int(math.pow(base, expo)))
