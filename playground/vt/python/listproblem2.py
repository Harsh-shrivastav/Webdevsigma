l = [3, 4, 0, 0, 6, 4, 5, 7,0,0,0,11,12,0,8]
z = []
n = []
for i in range(len(l)):
    if l[i] > 0 :
        n.append(l[i])
    else :
        z.append(l[i])
print("list:", n+z)
