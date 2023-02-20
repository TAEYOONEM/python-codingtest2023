tower1 = [5,4,3,2,1]
tower2 = []
tower3 = []


def hanoi(n) :
    global tower1,tower2,tower3
    while True :
        if move(tower1,tower2) :
            break
        elif move    

def move(arr1,arr2) :
    if len(arr2) == 0 or arr1[-1] < arr2[-1] :
        arr2.append(arr1[-1])
        arr1.pop() 
        return True
    else :
        return False

