def factors(num):
    return [i for i in range(1, num) if num % i == 0]


num = int(input("Enter the Number: "))
if sum(factors(num)) == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

