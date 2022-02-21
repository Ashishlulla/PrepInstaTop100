string = input("Enter the String : ")
lst = []
for i in string.split(" "):
    i = i[0].upper()+i[1:-1]+i[-1].upper()
    lst.append(i)


print(" ".join(lst))

