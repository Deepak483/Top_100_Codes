# Palindrome number
num = int(input("Enter the number: "))
rev_no = 0
temp = num
while num > 0:
    remainder = num % 10
    rev_no = rev_no * 10 + remainder
    num = num // 10

if temp == rev_no:
    print(f"Given number {temp} is Palindrome Number ")
else:
    print(f"Given number {temp} is Not Palindrome Number ")
