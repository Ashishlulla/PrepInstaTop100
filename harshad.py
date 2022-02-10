def is_harshad(num):
    add = 0
    for i in str(num):
        add = add + int(i)
    if num % add == 0:
        print("Harshad Number!!!")
    else:
        print("Not a Harshad Number")

is_harshad(378)
