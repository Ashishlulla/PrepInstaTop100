str1 = input("Enter the String: ")
new_string = ""
for i in str1:
    if (64 < ord(i) < 91) or (96 < ord(i) < 123):
        new_string+=i
    else:
        pass

print(new_string)
