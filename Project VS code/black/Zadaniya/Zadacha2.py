a = [11, 12, 13]
c = [31, 32]
b = [21, 22, min(c)]

x = int(input())

if x >= 1:
    y = max(b)
if -1 < x < 1:
    y = min(a)
if x <= -1:
    y = 1
    
print(y)