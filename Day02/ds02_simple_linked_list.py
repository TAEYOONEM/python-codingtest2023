# 단순 연결리스트 구현
class Node :
    def __init__(self) -> None:
        self.data = None
        self.link = None


# 전역변수
memory = []
head, current, pre = None,None,None
dataArrary = ['찬욱','창동','준호','상수','기덕']

def printNodes(start) :
    current = start
    if current == None :
        return 
    
    print(current.data, end=' -> ')
    while current.link != None :
        current = current.link
        if current.link == None :
            print(current.data)
        else :
            print(current.data, end=' -> ')

# 노드추가 
def insertNode(findData,insertData) :
    global memory, head, current, pre

    if head.data == findData :
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    current = head # 제일 앞으로
    while current.link != None :
        pre = current
        current = current.link
        if current.data == findData :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return 

    node = Node()
    node.data = insertData
    current.link = node
    return

# 노드삭제
def deletNode(deleteData) :
    global memory, pre, current, head

    if head.data == deleteData : # 첫번째 노드 삭제
        current = head
        head = head.link # 두번쨰 노드로 변경
        del(current)
        return

    current = head
    while current.link != None : # 첫번째 이외 노드 삭제
        pre = current # 모두 첫번째 노드가르킴
        current = current.link # 두번째 노드 가르킴
        if current.data == deleteData :
            pre.link = current.link # current 가리키는 노드를 pre가 가리키도록 (삭제) 
            del(current)
            return

# 노드검색
def findNode(findData) :
    global memory, pre, current, head
    
    current = head # 첫번째 노드부터
    if current.data == findData :
        return current
    while current.link != None :
        current = current.link # 다음노드
        if current.data == findData :
            return current
    
    return Node() # 빈노드 반환


if __name__ == '__main__' :
    node = Node()
    node.data = dataArrary[0]
    head = node
    memory.append(node)

    for data in dataArrary[1:] :
        pre = node
        node = Node()
        node.data = data
        pre.link = node 
        memory.append(node)

    printNodes(head) # 전체출력
 
    print('노드 추가 ----')

    insertNode('찬욱','놀란') # 맨앞에 
    printNodes(head)

    insertNode('기덕','왕가위') # 중간에
    printNodes(head)

    insertNode('고다르','스필버그') # 맨마지막 노드 추가
    printNodes(head)
    
    print('노드 삭제 ----')
    deletNode('기덕')
    printNodes(head)
    deletNode('스필버그')
    printNodes(head)
    deletNode('고다르') # 데이터 삭제 X
    printNodes(head)

    print('노드 검색 ----')
    
    result = findNode('찬욱')
    if result.data != None :
        print('데이터를 찾았습니다.')
    else :
        print(' 검색한 데이터 없습니다.')
    
    result = findNode('슌지')
    if result.data != None :
        print('데이터를 찾았습니다.')
    else :
        print(' 검색한 데이터 없습니다.')
