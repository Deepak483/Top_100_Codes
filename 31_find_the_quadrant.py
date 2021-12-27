x_co = int(input("X cordinate: "))
y_co = int(input("Y cordinate: "))

if x_co > 0 and y_co > 0:
    print("First quadrant!!")
elif x_co < 0 and y_co > 0:
    print("Second Quadrant!!")
elif x_co < 0 and y_co < 0:
    print("Third Quadrant!!")
elif x_co > 0 and y_co < 0:
    print("Fourth Quadrant!!")
else:
    print("Origin!!")
