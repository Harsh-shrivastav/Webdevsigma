l = [2, 4, 6, 17, 19, 12, 13]

for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j] > l[j+1]:
             l[j], l[j+1] = l[j+1], l[j]
print("the sorted list is:",l)

    