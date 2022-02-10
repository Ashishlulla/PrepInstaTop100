number = int(input("Enter the Number: "))
if len(str(number)) == 1:
    print("Ones")
elif len(str(number)) == 2:
    print("Tens")
elif len(str(number)) == 3:
    print("Hundreds")
elif len(str(number)) == 4:
    print("Thousands")
else:
    print("Invalid Input")