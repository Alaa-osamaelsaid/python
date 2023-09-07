#method1

#pi=3.14159
#radius= float(input("enter the radius of the circle: "))
#def area(value):
 #   return float(pi*(pow(value,2)))

#result= area(radius)
#print("area of circle: ",result)

#method2

import math
radius= float(input("enter the radius of the circle: "))
#using math library
area= math.pi*radius*radius
print("area of circle: ",area)