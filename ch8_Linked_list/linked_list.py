## Node 생성
class Node:
    def __init__(self,data):
        self.data = data # 노드에 저장 할 값
        self.next = None # 다음 노드에 대한 reference


def mk_linkedlist(input):
    head = Node(None)
    tail = Node(None)

    for i, val in enumerate(input,1):
        if i == 1:
            node = Node(val)
            head.next = node
        elif i == len(input):
            node = Node(val)
            node.next = tail
        else:
            node = Node(val)



