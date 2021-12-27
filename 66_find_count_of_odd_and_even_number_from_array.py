input_number = list(map(int, input().split()))
count_odd = 0
count_even = 0
for i in input_number:
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print("Even elements: " + str(count_even))
print("odd elements: " + str(count_odd))
