a1 = [2,4,6,9,15,16,19,20,55,66]
a2 = [3,7,8,12,14,17]

b = []
while a1 and a2:
    if a1[0] < a2[0]:
        b.append(a1.pop(0))
    else:
        b.append(a2.pop(0))
b.extend(a1 or a2) 

print(b)

