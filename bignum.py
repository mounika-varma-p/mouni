a=int(input("Enter a value"))
b=int(input("Enter b value"))
c=int(input("Enter c value"))
d=int(input("Enter d value"))
if a>b and a>c and a>d:
    print("A is big value")
elif b>a and b>c and b>d:
    print("B is big value")  
elif c>a and c>b and c>d:
    print("C is big value")
else:
    print("D is big value")  