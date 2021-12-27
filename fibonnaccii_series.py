def fibonacci_series(n):
    if n < 1:
        return -1
    else:
        return fibonacci_series(n-1) + fibonacci_series(n-2)


n = int(input("Enter the number of Fibonacci series you want:"))


for i in range(n-2):
    print(fibonacci_series(i), end=" ")
