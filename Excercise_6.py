def computepay():
    if(hrs>40):
        p=(hrs-40)*(rate)*(1.5)+(rate)*(40)
        return p
    else:
        p=rate*hrs
        return p
hrs = float(input("Enter Hours:"))
rate=float(input("Enter rate:"))
p = computepay()
print(p)
