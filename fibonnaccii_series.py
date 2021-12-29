def fibonacci_series(i):
    if i <= 1:
        return i
    else:
        return (fibonacci_series(i-1) + fibonacci_series(i-2))


n = int(input("Enter the number :"))
if n <= 0:
    print("Please enter a positive number :")
else:
    print("Fibonacci series  ", end=' ')
    for i in range(n):
        print(fibonacci_series(i), end=' ')
