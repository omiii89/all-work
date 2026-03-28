a="Enter What You have to Convert ? \n"
print(a)
print("1.Kilogram -> Gram")
print("2.Meter -> Centi meter")
print("3.celcius -> Farhient")
select = input("Select what you has to do -->  ")
print(select)
if(select=="1"):
    b=int(input("How Many Kg ? \n"))
    c= b*1000
    print(c,"g")
elif(select=="2"):
    e=int(input("How Many M ? \n"))
    f= e*100
    print(f,"cm")
elif(select=="3"):
    k=float(input("How Many c ? \n"))
    g= (k*9/5)+ 32
    print(g,"f")
else:
    print("CHoose Invaild😁")