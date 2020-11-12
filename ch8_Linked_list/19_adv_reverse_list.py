from linked_list import Node

lst_node1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)
lst_node1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5

"""
링크드 리스트 인덱스 m에서 n까지를 역순으로 만들어라, 인덱스는 1부터 시작
"""

def reverseBetween(head, m, n):
    root = start = Node(None)
    root.next = head

    for _ in range(m-1): # for문에서 컴포넌트가 필요없으면 _로 줘서 메모리 효율 높임
        start = start.next
    end = start.next

    for _ in range(n-m):
        # tmp : 엣지 변경으로 연결 끊긴 노드 주소를 저장하기 위해
        tmp, start.next, end.next = start.next, end.next, end.next.next 
        start.next.next = tmp

    return root.next