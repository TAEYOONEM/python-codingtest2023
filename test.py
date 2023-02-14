
# for i in range(1,n+1) :
#     if i == 1 :
#         continue
#     for j in range(2,int(i**0.5)+1) :
#         if i % j == 0 :
#             break
#     else :
#         print(i)


while True : 
    n = int(input())
    cnt = 0
    if n == 0 :
        break
    
    for i in range(n,2*n+1) :
        if i == 1 :
            continue
        for j in range(2,int(i**0.5)+1) :
            if i%j == 0 :
                break
        else :
            cnt += 1        
    print(cnt)
    
               