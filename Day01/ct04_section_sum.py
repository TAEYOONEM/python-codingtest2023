import sys
input = sys.stdin.readline # 입력속도 개선, 주피터 노트북에서는 실행불가

# n, m = map(int,input().split())
# arr = list(map(int,input().split()))
# for k in range(m) :
#     i,j = map(int,input().split())
#     x = sum(arr[i-1:j])
#     print(x) 

# n, m = map(int,input().split())
# arr = list(map(int,input().split()))
# temp = 0 
# prefix_sum = [0]
# for i in arr :
#     temp += i
#     prefix_sum.append(temp)
# for j in range(m) :
#     ii, jj = map(int,input().split())
#     print(prefix_sum[jj]-prefix_sum[ii-1])   

n ,m = map(int,input().split())
arr = list()
for i in range(n) :
    arr += [list(map(int,input().split()))]
print(arr)

# temp = 0
# prefix_sum = list()
 
# for i in range(n) :
#     for j in range(n) :
#         temp += arr[i][j]
#         prefix_sum[i][j] = temp 

# for i in range(m) :
#     x, y = map(int,input().split())
#     prefix_sum[x-1][y-1] - prefix_sum[x-1][y-3]
#     + prefix_sum[x-2][y-1] -prefix_sum[x-2][y-3]



