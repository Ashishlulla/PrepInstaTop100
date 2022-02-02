def is_armstrong(num):
    add = 0
    for i in str(num):
        add += int(i)**len(str(num))
    if add == num:
        return True
    else:
        return False

strt = int(input("Enter the Start: "))
end= int(input("Enter the End : "))
armstrong = [i for i in range(strt, end+1) if is_armstrong(i)]
print(armstrong)