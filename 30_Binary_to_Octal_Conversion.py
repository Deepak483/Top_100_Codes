# print("Enter the Binary Number :")
# binary_num = int(input())

# octal_num = ""
# octal_dig = 0
# mul = chk = 1

# while binary_num != 0:
#     rem = binary_num % 10
#     octal_dig = octal_dig + rem * mul
#     if chk % 3 == 0:
#         octal_num = octal_num + str(octal_dig)
#         mul = chk = 1
#         octal_dig = 0
#     else:
#         mul = mul * 2
#         chk = chk + 1
#         binary_num = int(binary_num/10)


# if chk != 1:
#     octal_num = octal_num + str(octal_dig)

# print("\n Equivalent Octal Value is ", octal_num[::-1])


# Octal Number using int() and oct()
print("Enter the binary number :", end=" ")
binary_num = input()

octal_num = int(binary_num, 2)
octal_num = oct(octal_num)
print("\n The octal number is ", octal_num)
