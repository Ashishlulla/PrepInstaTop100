month = input("Enter the Number: ")
if month == "February":
    print("28/29 Days")
elif month in ("January", "March", "May", "July", "August", "October", "December"):
    print("31 Days")
elif month in ("April", "June", "September", "November"):
    print("30 Days")
else:
    print("Invalid Input or Incorrect Month Name")
