import math
x = int(input())
if x < 0:
    y = math.sin(x)
elif x > 1:
    y = math.tan(x)
else:
    y = math.cos(x)
print(y)
    