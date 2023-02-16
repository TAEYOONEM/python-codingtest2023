import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(sys.stdin.readline().rstrip())

arr.sort()
arr.sort(key=lambda x:len(x))
result = []

for i in arr :
    if i not in result :
        result.append(i)
        print(i)


