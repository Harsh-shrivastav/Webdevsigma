l = [2,6,10,17,19,27,23]
e = []
o = []
for i in range (len(l)):
    if l[i]%2 == 0:
        e.append(l[i])
    else:
        o.append(l[i])
print("even list:", e)
print("odd list:", o)


        