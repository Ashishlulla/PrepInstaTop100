def factorial(num):
    fact = 1
    if num == 1 or num==0:
        return 1
    else:
        while num > 0:
            fact = fact * num
            num -= 1
    return fact

number = int(input("Enter the Number"))
add = 0
for i in str(number):
    add = add + factorial(int(i))

if add == number:
    print("Strong Number")
else:
    print("Not a Strong Number")
