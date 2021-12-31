arr = list(map(int, input("Enter Array Elements: ").split()))
ans = -1
for i in range(0, len(arr)):
    if sum(arr[:i]) == sum(arr[i+1:]):
        ans = i
        print(f"Equilibrium index of an array:")
        break
print(ans)
