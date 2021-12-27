# finding symmetric pairs in arrays

def find_symmetric_pair(arr, n):

    hm = dict()
    for i in range(n):
        first = arr[i][0]
        sec = arr[i][1]
        if(sec in hm.keys() and hm[sec] == first):
            print('(', sec, ",", first, ")")
        else:
            hm[first] = sec


arr = []
n = int(input("Enter the number of pairs: "))
for i in range(0, n):
    l = list(map(int, input().split()))
    arr.append(l)

print("Symmetric element in array: ")
find_symmetric_pair(arr, n)
