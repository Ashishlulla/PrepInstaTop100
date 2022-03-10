a = [10, 20, 30, 40, 40, 50, 50, 50]
dict1 = dict(sorted({i:a.count(i) for i in a}.items(),key=lambda x:x[1], reverse=True))
ans = []
for key,val in dict1.items():
    for i in range(val):
        ans.append(key)

print(ans)
