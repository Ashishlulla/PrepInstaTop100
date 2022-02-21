str1 = input("Enter the String: ")
vowels = "AEIOUaeiou"
count = 0
for i in str1:
    if i in vowels:
        count +=1
    else:
        pass

print(f"vowels count is : {count}")