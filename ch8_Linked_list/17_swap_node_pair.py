from linked_list import Node

lst_node1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
lst_node1.next = node_2
node_2.next = node_3
node_3.next = node_4

# my(단순 값 swap)
"""
변칙적인 풀이, 시공간 복잡도는 괜찮으나 좋은 코드가 아니다. 온라인 코테에선 괜찮다.
"""
def swap_pair(head):
    lst = head # node의 reference를 updt 하므로, 새로운 객체에 할당해서 swap 작업 실시 

    while lst and lst.next:
        lst.next.data, lst.data = lst.data,lst.next.data
        lst = lst.next.next

    return head


# 연결 리스트 구조 swap(연결 edge 수정)
def swap_pair2(head):
    root = prev = Node(None) # prev reference를 updt 하므로 return할 root 따로 선언
    prev.next = head

    while head and head.next:
        b = head.next
        head.next = b.next
        b.next = head

        prev.next = b

        head = head.next
        prev = prev.next.next
    
    return root.next
        
