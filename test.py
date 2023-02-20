<<<<<<< Updated upstream
import sys
<<<<<<< Updated upstream
cnt = 0
def mergeSort(arr) : 
    
    global cnt
=======
x666 666x x666 x666x 666xx x666x  
>>>>>>> Stashed changes

    if len(arr) < 2 :
        return arr
    
    mid = len(arr) // 2
    left_arr = mergeSort(arr[:mid])
    right_arr = mergeSort(arr[mid:])

<<<<<<< Updated upstream
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
=======
num = 666
x = 0
x += 1  
num += x*1000
if x = 9
num *= 10
>>>>>>> Stashed changes

input = sys.stdin.readline
n, k = map(int,input().split())
arr = list(map(int,input().split()))
mergeSort(arr)
=======
n = int(sys.stdin.readline()) 
arr = list(map(int,sys.stdin.readline().split()))
result = sorted(list(set(arr)))
for i in arr :
    print(result.index(i),end=' ')
>>>>>>> Stashed changes
