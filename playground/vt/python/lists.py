l = [2,6,10,17,19,27,23]
e = []
o = []
for i in range (len(l)):
    if i%2 == 0:
        e.append(i)
    else:
        o.append(i)
print("even list:", e)
print("odd list:", o)


        