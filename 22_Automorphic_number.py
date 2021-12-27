n = int(input("Enter the number :"))
# convert the n into string and find the lenght of it
num_of_digit = len(str(n))


# calculate the square
square = n ** 2

# calculate the last digit
last_digit = square % pow(10, num_of_digit)

if last_digit == n:
    print(f"{n} is Automorphic Number!!")
else:
    print(f"{n} is no Automorphic Number!!")
