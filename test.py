import sys
cnt = 0
def mergeSort(arr) : 
    
    global cnt

    if len(arr) < 2 :
        return arr
    
    mid = len(arr) // 2
    left_arr = mergeSort(arr[:mid])
    right_arr = mergeSort(arr[mid:])

    l = r = 0
    tmp=[]

    while l < len(left_arr) and r < len(right_arr) :
        
        if left_arr[l]  < right_arr[r] :
            tmp.append(left_arr[l])
            l += 1
        else :
            tmp.append(right_arr[r])
            r += 1

    if l >= len(left_arr) :
        tmp += right_arr[r:]
    else :
        tmp += left_arr[l:]
    
    return tmp

input = sys.stdin.readline
n, k = map(int,input().split())
arr = list(map(int,input().split()))
mergeSort(arr)