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

# 노드 추가 
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

    printNodes(head)
