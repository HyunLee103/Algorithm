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
Leetcode 328
linked list를 홀수 노드 다음 짝수 노드가 오게 재구성해라
"""

def odd_even(head):
    odd = head
    even = head.next
    even_head = head.next # even의 reference가 변화하므로, 홀수와 연결할 짝수 head 객체 따로 선언

    while even and even.next:
        odd.next = odd.next.next
        odd = odd.next
        even.next = even.next.next
        even = even.next

    odd.next = even_head

    return head

k = odd_even(lst_node1)
