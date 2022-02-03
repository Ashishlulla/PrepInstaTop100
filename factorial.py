def factorial(num):
    fact = 1
    if num == 1 or num==0:
        return 1
    else:
        while num > 0:
            fact = fact * num
            num -= 1
    return fact

print(factorial(5))