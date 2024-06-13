# import numpy
# import matplotlib
import math

names = ['Molly', 'Fleetwood','Hamburglar','Spoonman']
for name in names:
    print(name)

a=int(input("What is the value of a?"))
b=int(input("What is the value of b?"))
c=int(input("What is the value of c?"))

axis_sym=(-1*b)/(2*a)
print("Axis of symmetry is x=",axis_sym)

max_min=a*((axis_sym)**2+b*axis_sym+c)
if a>0:
    print("The parabola is concave down. The minimium value is ", max_min)
else:
    print("The parabola is concave up. The maximum value is ", max_min)

x_smaller=round((-1*b- math.sqrt(b**2-4*a*c))/(2*a),2)
x_larger=round((-1*b + math.sqrt(b**2-4*a*c))/(2*a),2)



if (a>b) :
    print("a is greater ")
else :
    print("b is greater")
    

