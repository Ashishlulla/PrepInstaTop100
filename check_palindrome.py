def is_palindrome(string):
    return string == string[::-1]


str1 = input("Enter the String: ").lower()
print(is_palindrome(str1))