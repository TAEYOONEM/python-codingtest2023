import sys 
input = sys.stdin.readline

N = int(input())
cnt = 0
a = list(map(int,input().split()))
a.sort()

for k in range(N) :
    find = a[k]
    i = 0; j = N-1
    while i < j :
        if a[i] + a[j] == find : 
            if i != k and j != k :
                cnt += 1
                break
            elif i == k : i += 1
            elif j == k : j -= 1 
        elif a[i] + a[j] < find : 
            i += 1
        elif a[i] + a[j] > find : 
            j -= 1
print(cnt)           
