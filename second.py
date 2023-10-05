x = int(input())
p = float(input())
y = int(input())

for i in range(1, 1000000):
    if x>=y:
    	break
    x += round(x* (p / 100), 2)
print(i)