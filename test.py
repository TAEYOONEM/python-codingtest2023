n = int(input())

max = 0

arr = [None for _ in range(n)] # 입력
for i in range(n) :
    arr[i] = int(input())
    if arr[i] > max :
        max = arr[i]

brr = [0 for _ in range(max+1)] # 등장 횟수
crr = [0 for _ in range(max+1)] # 누적합

for i in range(n) :
    brr[arr[i]] += 1 

for i in range(1,n+1) :
    for j in range(1,i+1) :
        crr[i] += brr[j]  

drr = [None for _ in range(n)]
for i in arr :
    drr[crr[i]] = i
    crr[i] -= 1

print(drr) 
