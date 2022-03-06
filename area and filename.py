import math as M
Radius = float (input ("Please enter the radius of the given circle: "))
area=M.pi* Radius * Radius
print (" The area of the  circle with radius is:",area)
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
