#Input a number (X) and create a program that allows 
#the user to select finding the area (Area) 
#of one of the following:
#● The area of a square with side X, Area = X * X
#● The area of a circle with radius X, Area = 3.14 * X^2
#● The area of an equilateral triangle with side X, 
#Area = Sqrt(3)/4 * X^2
#Note: Because X represents a dimension, 
#we require that X > 0. 
#Be sure to include this requirement in your program.
import math

x = int(input("Enter  a number: "))

if x<0 :
    print("\nEnter a number greater than 0")
elif x > 0 :
    option=int(input("\nEnter 1-3 to select an option\n"+
        "1. Square\n" +
          "2. Circle\n" +
          "3. Triangle\n\n"+
          "Choice: "))
    if option == 1:
        areaofsquare= math.pow(x, 2) 
        print(f"the area of a square is : {areaofsquare}")
    elif option == 2:
        areaofacircle= math.pi * math.pow(x, 2)
        print(f"the area of the circle is: { areaofacircle}")
    elif option == 3: 
        areaOfTriangle = math.sqrt(3)/4 * math.pow(x, 2)
        print(f"area of an equilateral triangle:{areaOfTriangle}")
    else:
        print("Invalid number. Must be 1, 2, or 3 ")
