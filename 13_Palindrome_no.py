# Palindrome number
num = int(input("Enter the number :"))
temp = num
rev_num = 0
while num > 0:
    remainder = num % 10
    rev_num = rev_num * 10 + remainder
    num = num // 10

if rev_num == temp:
    print(f"{temp} is Palindrome Number!!")
else:
    print(f"{temp} is Not Palindrome Number!!")
