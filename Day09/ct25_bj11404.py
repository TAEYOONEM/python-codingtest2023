import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
distance = [[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]

for i in range(1,N+1) :
    distance[i][i] = 0

for i in range(M) :
    start, end, cost = map(int,input().split())
    if distance[start][end] > cost : # 중복된 노선 중 더 저렴한 거
        distance[start][end] = cost
        
for k in range(1,N+1) :
    for i in range(1,N+1) :
        for j in range(1,N+1) :
            if distance[i][j] > distance[i][k] + distance[k][j] :
               distance[i][j] = distance[i][k] + distance[k][j]

for i in range(1,N+1) :
    for j in range(1,N+1) :
        if distance[i][j] != sys.maxsize :
            print(distance[i][j],end=" ")
        else :
            print(0,end=" ")
    print()