Number = int(input("Enter the range of  number :"))
divisor = int(input("Enter the divisor: "))

count1 = 0
for i in range(1, Number + 1):
    count2 = 0
    for j in range(1, i+1):
        if i % j == 0:
            count2 += 1
        else:
            pass
    if count2 == divisor:
        count1 += 1
        print(i, end=' ')

print(" ")
print(count1)
