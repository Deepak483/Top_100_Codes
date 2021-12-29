def SumOfNumber(n):
    if n == 0:
        return 0
    else:
        return n + SumOfNumber(n-1)


n = int(input("Enter the number: "))
print(SumOfNumber(n))
