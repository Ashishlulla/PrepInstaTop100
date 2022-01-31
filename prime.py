def is_prime(num):
    factors = [i for i in range(2, num) if num%i==0]
    if len(factors) == 0:
        print("Prime Number")
    else:
        print("Not a prime Number")

is_prime(17)
