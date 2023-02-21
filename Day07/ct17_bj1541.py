answer = 0
A = list(map(str,input().split('-')))

def mySum(i) :
    result = 0
    tmp = str(i).split('+')
    for k in tmp : 
        result += int(k)
    return result

for s in range(len(A)) :
    tmp = mySum(A[s])

    if s == 0 :
        answer += tmp
    else :
        answer -= tmp

print(answer)