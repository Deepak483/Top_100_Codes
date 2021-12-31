arr = [19, 9, 16, 6, 3, 2, 11, 18, 27]
a = sorted(arr)
print(a)
# [2, 3, 6, 9, 11, 16, 18, 19, 27]
res = []
for i in arr:
    res.append(a.index(i)+1)

print(res)
