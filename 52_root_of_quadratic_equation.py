# b**2-4*a*c
# this program is to find out the root of ax*2 + bx + c
import math
a = int(input("enter the value of a: "))
b = int(input("enter the value of b: "))
c = int(input("enter the value of c: "))

if a == 0:
    print("a cannot be zero")
else:
    val = b**2 - 4*a*c
    root = math.sqrt(abs(val))
    if val > 0:
        print("two real root")
        print((-b+root)/(2*a))
        print((-b-root)/(2*a))
    elif val == 0:
        print("only one root possible ")
        print((-b/(2*a)))
    else:
        print("No real root")
        print((-b/(2*a)), "+ i", root)
        print((-b/(2*a)), "- i", root)
