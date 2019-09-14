hrs =input("Enter Hours:")
h = float(hrs)
b=input("Enter RATE:")
basic_rate=float(b)
if h <=40:
   pay = h * basic_rate
elif h > 40:
   pay = 40* basic_rate + (h-40)*1.5*basic_rate  
print(pay)
