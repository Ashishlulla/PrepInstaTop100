def HCF(num1, num2):
    factor_1 = [i for i in range(1, num1 + 1) if num1 % i == 0]
    factor_2 = [i for i in range(1, num2 + 1) if num2 % i == 0]
    return max(set(factor_1).intersection(set(factor_2)))


def lcm(a, b):
    return (a * b) // HCF(a, b)


print(lcm(3, 4))
