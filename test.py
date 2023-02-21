
import sys

ans = []
def mergeSort(arr) :    
    global ans
    if len(arr) == 1 :
        return arr
    
    mid = (len(arr)+1) // 2
    left_arr = mergeSort(arr[:mid])
    right_arr = mergeSort(arr[mid:])

    l = r = 0
    tmp=[]

    while l < len(left_arr) and r < len(right_arr) :   
        if left_arr[l]  < right_arr[r] :
            tmp.append(left_arr[l])
            ans.append(left_arr[l])
            l += 1
        else :
            tmp.append(right_arr[r])
            ans.append(right_arr[r])
            r += 1

    if l >= len(left_arr) :
        tmp += right_arr[r:]
        ans +=  right_arr[r:]
    else :
        tmp += left_arr[l:]
        ans +=  left_arr[l:]
    
    return tmp


input = sys.stdin.readline
n, k = map(int,input().split())
arr = list(map(int,input().split()))
mergeSort(arr)
if k <= len(ans) :
    print(ans[k-1])
else :
    print(-1)

