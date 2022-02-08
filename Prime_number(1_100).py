def is_prime(num):
    flag = 0
    for i in range(2, num):
        if num % i == 0:
            flag = 1
            break
        else:
            pass
    if flag == 0:
        return True
    else:
        return False


print([i for i in range(1, 101) if is_prime(i)])
