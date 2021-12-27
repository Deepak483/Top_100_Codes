import math

N = int(input("Enter the number of people or things :"))
R = int(input("Enter the number of seats or place: "))

N_fact = math.factorial(N)
N_minus_R = math.factorial(N-R)

no_of_ways = N_fact // N_minus_R

print("The of number of ways: ", no_of_ways)
