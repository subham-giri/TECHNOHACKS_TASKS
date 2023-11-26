def addcalc(a,b):
    return(a+b)
def subcalc(a,b):
    return(a-b)
def mulcalc(a,b):
    return(a*b)
def divcalc(a,b):
    return(a/b)
a=int(input("enter a number"))
b=int(input("enter another number"))
print("enter a number \n1.add \n2.sub \n3.mul \n4.div")
c=int(input("enter number:"))

if c==1:
    d=addcalc(a,b)
    print("sum of two numbers is:",d)
elif c==2:
    e=subcalc(a,b)
    print("sub of two numbers is",e)
elif c==3:
    f=mulcalc(a,b)
    print("mul of two numbers is",f)
elif c==4:
    g=divcalc(a,b)
    print("div of two numbers is",g)
else:
    print("enter a valid number for operation")