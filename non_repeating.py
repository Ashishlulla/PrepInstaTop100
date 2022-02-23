string = input("Enter the String: ")
print("Non repeating characters are: ")
for i in string:
    if string.count(i) == 1:
        print(i, end=",")
    else:
        pass