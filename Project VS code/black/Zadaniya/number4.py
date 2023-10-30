x=1.4444
b=0.318
t=2.1
a=1.3
import math
y = (9*x**2) + (math.sin(x)**2)*math.sqrt(a-b)
print ("y = ", y)
z = ((x**t)**(1/3)) * (a*(x**3)-(x**2)/math.factorial(2))
print("z = ", z)