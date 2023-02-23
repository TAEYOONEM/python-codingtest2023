def drawStar(n) :
    if n == 1:
        return '*'
    stars = drawStar(n//3)
    L = []

    for i in stars :
        L.append(i*3)
    for i in stars :
        L.append(i+" "*(n//3)+i)
    for i in stars :
        L.append(i*3)

    return L

n = int(input())
print("\n".join(drawStar(n)))