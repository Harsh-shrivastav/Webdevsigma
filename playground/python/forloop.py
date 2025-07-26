for i in range(1,10):
    print(i)
 
for i in range(10,0,-1):
    print(i)



count = 0
n = int(input("enter a number:"))
for i in range(2,n):
    if n%i == 0:
        count = count + 1
if count == 0:
    print("prime")
else:
    print("not prime")

a = int(input("enter a number:"))
if a%2 == 0:
    print("even")
else:
    print("odd")


even_count = 0
odd_count = 0
for i in range(1,11):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers: ",{even_count})
print("Odd numbers:", {odd_count})

even_count = 0
odd_count = 0
a = int(input("enter a number:"))
b = int(input("enter a number:"))
for i in range(a,b+1):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("even numbers are:", even_count)
print("odd numbers are:", odd_count)