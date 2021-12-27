def factorial_no(num):
    if num == 0 or num == 1:
        return 1
    elif num < 0:
        print("Please enter the positive number ")
    else:
        return (num)*factorial_no(num-1)


num = int(input('enter the number you want the factorial of :'))
if factorial_no(num) is not None:
    print("Factorial of the number is ", factorial_no(num))
