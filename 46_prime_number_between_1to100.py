prime_number = []
for i in range(2, 101):
    flag = 0
    for j in range(2, i+1):
        if (i != j and i % j == 0):
            flag = 1
            break
    else:
        prime_number.append(i)

print(prime_number)
