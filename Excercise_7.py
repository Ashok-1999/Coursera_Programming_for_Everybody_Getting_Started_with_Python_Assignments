largest = None
smallest = None
while True:
    inp = input("Enter a number: ")
    if inp == "done" : 
        break
    try:
        num = int(inp)
    except:
        print('Invalid input')
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
    elif num > largest:
        largest = num
    continue
print("Maximum is", largest)
print("Minimum is", smallest)