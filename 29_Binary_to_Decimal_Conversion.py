# Code is written for binary to decimal conversion
num = int(input("Enter the Binary Number: "))
binary_num = num
decimal_num = 0
base = 1

# condition checking the number is greater than 0 or not
while num > 0:
    rem = num % 10
    decimal_num = decimal_num + rem * base
    num = num // 10
    base = base * 2

print(f" Binary Number is {binary_num} and Decimal Number is {decimal_num} ")
