print("enter 1 for celcius \nenter 2 for fahrenheit ")
a=int(input("enter 1 or 2 "))
if a==1:
    b=int(input("enter temperature in celcius"))
    c=b*(9/5)+32
    print(b,"degree celcius is:\n",c,"degree fahrenheit")
elif a==2:
    d=int(input("enter temperature in fahrenheit"))
    e=(d-32)*5/9
    print(d,"degree fahrenheit is\n", e,"degree celcius")
else:
    print("enter a valid value")