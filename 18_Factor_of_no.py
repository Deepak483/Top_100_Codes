num = int(input("Enter the num you want the factor of :"))
for i in range(1, num+1):
    if num % i == 0:
        print(f'{i}X{num//i}', end=' ')
