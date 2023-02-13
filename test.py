class Point() :
    x = 0
    y = 0

n = int(input())    
arr = [_ for _ in range(n)]
 
for i in range(n) :
    arr[i] = Point()
    arr[i].x,arr[i].y = list(map(int,input().split()))

temp = Point()
min = 0

for i in range(n-1) :
    min = i
    for j in range(i,n) :
        if arr[min].x > arr[j].x :
            min = j  
    if arr[i].x > arr[min].x :
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
    elif arr[i].x == arr[min].x :
        if arr[i].y > arr[min].y :
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp
    
for i in range(n) :
    print(arr[i].x,arr[i].y)

# arr = [2,1,3,5,4]

# min = 0
# temp = 0

# for i in range(4) :
#     min = i
#     for j in range(i,5) :
#         if arr[j] < arr[min] :
#             min = j
#     if arr[i] > arr[min] :
#         temp = arr[i]
#         arr[i] = arr[min]
#         arr[min] = temp  

# print(arr)