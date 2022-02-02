def is_abundant(num):
    a = [i for i in range(1, num) if num % i == 0]
    if sum(a) > num:
        print("Abundant Number!!!")
    else:
        print("Not Abundant Number!!!")

is_abundant(12)