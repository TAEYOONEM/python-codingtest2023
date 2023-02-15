# Queue 구현
# 전역변수

SIZE = 0
queue =[]
front, rear = -1,-1

# Check Queue Full 
def isQueueFull() :
    global SIZE,queue,front,rear

    if rear != SIZE - 1 :
        return False
    elif rear == SIZE -1 and front == -1 :
        return True
    else :
        for i in range(front+1,SIZE) :
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False


# Check Queue Empty
def isQueueEmpty() :
    global SIZE,queue,front,rear

    if front == rear :
        return True
    else :
        return False

# Insert Queue data
def enQueue(data) : 
    global SIZE,queue,front,rear

    if isQueueFull() :
        print("Queue is full")
    else :
        rear += 1
        queue[rear] = data

def deQueue() :
    global SIZE,queue,front,rear
    
    if isQueueEmpty() :
        print("Queue is empty") 
        return None
    else :
        front += 1
        data = queue[front]
        queue[front] = None
        
        for i in range(front+1,SIZE) :
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        
        return data

def peek() :
    global SIZE,queue,front,rear

    if isQueueEmpty() :
        print("Queue is empty") 
        return None
    else :
        return queue[front+1]

if __name__ == "__main__" :
    SIZE = int(input("Input Queue size >>"))
    queue = [None for _ in range(SIZE)]

    while True :
        select = input("Insert data(I),Extract(E),Verify(V),Exit(X) >>")
        if select.lower() == 'x' :
            break
        elif select.lower() == 'i' :
            data = input("data >>")
            enQueue(data)
            print(f"Queue status : {queue}")
        elif select.lower() == 'e' :
            data = deQueue()
            print(f"Extracted data : {data}")
            print(f"Queue status : {queue}")
        elif select.lower() == 'v' :
            data = peek()
            print(f"Verified data : {data}")
            print(f"Queue status : {queue}")
        else  :
            continue 
    
    print("Exit Queue Program")



    







