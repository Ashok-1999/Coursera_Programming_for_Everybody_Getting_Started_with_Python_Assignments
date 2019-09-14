score = input("Enter Score: ")
a=float(score)
if a > 1:
     print('Enter a numeric between 0 to 1')
elif a >= 0.9 :
    print('A')
elif a >= 0.8 :
    print('B')
elif a >= 0.7:
    print('C')
elif a >= 0.6:
    print('D')
elif a >= 0:
    print('F')
else:
    print('Enter a numeric between 0 to 1')