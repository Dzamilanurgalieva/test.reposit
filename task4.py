a = float(input())
b = float(input())
c = float(input())
max1 = float()
if a >= b and a >= c:
    max1 = a
elif b >= a and b >= c:
    max1 = b
elif c >= a and c >= b:
    max1 = c
print(max1)

