def is_prime(num):
    factors = [i for i in range(2,num) if num % i == 0]
    if len(factors) == 0:
        return True
    else:
        return False

num = int(input("enter the Number"))
factors = [i for i in range(2,num) if num % i == 0]
prime_factors = [i for i in factors if is_prime(i)]
for j in prime_factors:
    print(j ,end=" ")
