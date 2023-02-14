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
    