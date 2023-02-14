# 스택 전체구현

# 글로벌 변수
SIZE = 0
stack = []
top = -1 

# 스택이 꽉 찼는지 여부확인
def isStackFull() :
    global SIZE, stack, top # 전역변수를 그대로 함수에서도 사용
    if top >= SIZE - 1 :
        return True
    else : 
        return False

# 스택이 비어있는지 여부확인
def isStackEmpty() :
    global SIZE, stack, top 
    if top == - 1 :
        return True
    else : 
        return False


# 스택에 데이터 추가
def push(data):
    global SIZE, stack, top 
    if isStackFull() :
        print("Stack is full")
        return 
    else :
        top +=1 
        stack[top] = data

# 스택에서 데이터 추출 
def pop() :
    global SIZE, stack, top 
    if isStackEmpty() :
        print("Stack is empty")
        return None
    else :
        data = stack[top]
        stack[top] = None
        top -= 1
        return data

# top 데이터 확인
def peek() :
    global SIZE, stack, top 
    if isStackEmpty() :
        print("Stack is empty")
        return None
    else :
        return stack[top]

# main entry
'''
if __name__ == '__main__' :
    top = -1 
    SIZE = int(input('Input stack size >>'))
    stack = [None for _ in range(SIZE)]
    
    while True :
        select = input("Insert data(I),Extract(E),Verify(V),Exit(X) >>")
        if select.lower() == 'x': 
            break
        elif select.lower() == 'i' :
            data = input('Insert data >>') 
            push(data)
            print(f'Stack status: {stack}')
        elif select.lower() == 'e' :
            data = pop() 
            print(f'Extracted data : {data}')
            print(f'Stack status: {stack}')
        elif select.lower() == 'v' :
            data = peek()
            print(f'Verified data : {data}')
            print(f'Stack status: {stack}')
        else :
            continue

    print("Stack program Exit")
'''