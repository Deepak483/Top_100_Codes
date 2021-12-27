def fibonacci_series(i):
    if i <= 1:
        return i
    else:
        return fibonacci_series(i-1) + fibonacci_series(i-2)


num = int(input('Enter the number you want to find the fibonacci'))
if num <= 0:
    print("Please enter the postive number")
else:
    print("Fibnocci series of the number is ", end=' ')
    for i in range(num):
        print(fibonacci_series(i), end=' ')
