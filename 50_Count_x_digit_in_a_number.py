# Algorithm
# Step 1:- Start.
# Step 2:- Take input from the user.
# Step 3:- Take input of a digit whose occurrence is to be found.
# Step 4:- Change the datatype of the integer inputs.
# Step 5:- use the count function to count the occurrence of the digit and print it.
# Step 6:- End.

number = int(input("Enter the number: "))
digit = int(input("Enter the digit to be found: "))

string1 = str(number)
string2 = str(digit)

# using count function of python
count_of_digit = string1.count(string2)
print(f"Number of digit present in {number} is {count_of_digit}")
