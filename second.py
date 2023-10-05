import math

def area(a, b ,c):
    if a+c >b and a+b > c and b+c>a:
        p = ((a+b)+c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s
a = int(input())
b = int(input())
c = int(input())

result = area(a, b, c)
print(result)