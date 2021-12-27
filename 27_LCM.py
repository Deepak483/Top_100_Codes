def lcm_finder(num1, num2):

    if num1 > num2:
        larger = num1
    else:
        larger = num2

    while True:
        if (larger % num1 == 0 and larger % num2 == 0):
            lcm = larger
            break
        else:
            larger += 1

    print(f"lcm of {num1} and {num2} is {lcm}")


num1 = int(input("Enter the first  number :"))
num2 = int(input("Enter the second number "))
lcm_finder(num1, num2)
