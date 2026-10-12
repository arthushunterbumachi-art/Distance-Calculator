import math

# Ask the user to enter the coordinates of the first point
print("This is a distance calculator, pls input needed variables to calculate distance:")
x1 = float(input("Enter coordinate x1: "))
y1 = float(input("Enter coordinate y1: "))

# Ask the user to enter the coordinates of the second point
x2 = float(input("Enter coordinate x2: "))
y2 = float(input("Enter coordinate y2: "))

# Compute the distance using the distance formula
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Display the result rounded to two decimal places
print(f"The distance between the two points is: {distance:.2f}")
