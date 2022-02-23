str1 = input("Enter the String: ")
vowels = "AEIOUaeiou"
new_string = ""
for i in str1:
    if i in vowels:
        pass
    else:
        new_string +=i

print(f"After removing vowels : {new_string}")