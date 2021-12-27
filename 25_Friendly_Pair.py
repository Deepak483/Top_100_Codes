
n1 = int(input("Enter the number one"))
n2 = int(input("Enter the number two"))

sum1 = 0
sum2 = 0
for i in range(1, n1+1):
    if n1 % i == 0:
        sum1 += i

for i in range(1, n2+1):
    if n2 % i == 0:
        sum2 += i

abundacy_index1 = sum1//n1
abundacy_index2 = sum2//n2

print(sum1)
print(sum2)

if abundacy_index1 == abundacy_index2:
    print(f"{n1} and {n2} are Friendly Pair")
else:
    print(f"{n1} and {n2} are not Friendly Pair")
