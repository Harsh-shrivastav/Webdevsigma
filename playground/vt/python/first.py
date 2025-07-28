# sum of two numbers 
a = 5
b = 10 
c = a + b
print(c)


# basic calulation
a = int(input("enter the first number :"))
b = int(input("enter the second number :"))
c = input("enter the operator(+,-,*,/):")
if c == '+':
    print("add is" ,a+b)
elif c == '-':
    print("substraction is ",a-b) 
elif c == '*':
    print("multiply is" ,a*b)
elif c == '/':
    if b == '0':
        print("error")
    else:
        print("div is:",a/b)
else:
    print("invalid operator") 
    


#comparison between two numbers
a = 10
b = 20
if a == b:
    print("both are equal")
elif a > b:
    print("a is greater")
else:
    print("b is greater")
