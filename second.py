k = [10, 5,'asdf', 5, 15, 30, 'asdf']
z = []
repeat = []
for i in k:
    if i not in z:
        z.append(i)
    else:
        repeat.append(i)
print(repeat)