def is_prime(num):
    factors = [i for i in range(2, num) if num % i==0]
    if len(factors) == 0:
        return True
    else:
        return False


rng = int(input("Enter the Range: "))
primes = [i for i in range(2, rng+1) if is_prime(i)]
for i in range(len(primes)):
    for j in primes[i+1:]:
        if primes[i] + j == rng:
            print(f"{primes[i]} and {j} are the primes numbers when added gives {rng}")
        else:
            pass
