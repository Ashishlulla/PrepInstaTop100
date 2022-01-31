def is_prime(num):
    factors = [i for i in range(2, num) if num%i==0]
    if len(factors) == 0:
        return True
    else:
        return False


rng = int(input("Enter the Range: "))
primes = [i for i in range(1, rng+1) if is_prime(i)]
print(primes)
