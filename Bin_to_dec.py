def binary_to_decimal(num):
    base = 1
    value = 0
    while num > 0:
        rem = num % 10
        value += rem * base
        num = num // 10
        base = base * 2
    return value


print(binary_to_decimal(10))
