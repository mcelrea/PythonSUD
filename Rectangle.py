'''
Types of Variables
-----------------------
Type    Description        Notes
int     Integer            any whole number
float   Floating point     any real number (3.23)
str     String             words, characters
'''

a=float(input("Enter rectangle width: "))
b=float(input("Enter rectangle height: "))

answer=a/b-2

print("The Answer")
print("---------------------------------------------------")
print("The area of a rectangle with width", a, "and height",
      b, "is", answer)
print("---------------------------------------------------")