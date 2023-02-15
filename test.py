n = int(input())

max = 0

arr = [None for _ in range(n)] # 입력
for i in range(n) :
    arr[i] = int(input())
    if arr[i] > max :
        max = arr[i]

cnt_arr = [0 for _ in range(max+1)] # 등장 횟수
sum_arr = [0 for _ in range(max+1)] # 누적합

for i in range(n) :
    cnt_arr[arr[i]] += 1 

sum_arr[0] = cnt_arr[0]
for i in range(1,max+1) :
    sum_arr[i] = sum_arr[i-1] + cnt_arr[i]



