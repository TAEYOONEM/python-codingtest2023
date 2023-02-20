n = int(input())
a = [0] * int(n+1)
tmp = [0] * int(n+1)

for i in range(1, n+1) :
    a[i] = int(input())

a = sorted(a, reverse= False)

for i in range(1, n+1) :
    print(a[i])