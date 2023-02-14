n = int(input())

max = 0

arr = [None for _ in range(n)]
for i in range(n) :
    arr[i] = int(input())
    if arr[i] > max :
        max = arr[i]

brr = [0 for _ in range(max+1)]
for i in range(n) :
    brr[arr[i]] += 1 

crr = [None for _ in range(n)] 
for i in arr :
    crr[brr[i]] = i 
    brr[i] -= 1

print(arr)
print(brr)
print(crr) 