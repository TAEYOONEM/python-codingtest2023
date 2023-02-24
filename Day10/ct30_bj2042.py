import sys
input = sys.stdin.readline

N, M, K = map(int,input().split())
treeHeight = 0
length = N

while length != 0:
    length //= 2
    treeHeight += 1

treeSize = pow(2,treeHeight + 1)
leftStartIndex = treeSize // 2 - 1
tree = [0] * (treeSize+1)

for i in range(leftStartIndex+1,leftStartIndex + N +1) :
    tree[i] = int(input())

def setTree(i) :
    while i != 0 :
        tree[i//2] += tree[i]
        i -= 1
setTree(treeSize-1)

def chageVal(i, val) :
    diff = val - tree[i]
    while i > 0 :
        tree[i] += diff
        i //= 2

def getSum(s,e) :
    partSum = 0
    while s<= e :
        if s % 2 == 1 :
            partSum += tree[s]
            s += 1
        if e % 2 == 0 :
            partSum += tree[e]
            e -= 1
        s //= 2
        e //= 2
    return partSum

for _ in range(M+K) :
    q,s,e = map(int,input().split())
    if q == 1 :
        chageVal(leftStartIndex+s,e)
    elif q == 2 :
        s += leftStartIndex
        e += leftStartIndex
        print(getSum(s,e))
