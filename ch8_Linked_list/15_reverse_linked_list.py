from linked_list import Node


node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_1.next = node_2
node_2.next = node_3


def reverse_linkedlist(head):
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev
        
k = reverse_linkedlist(node_1)
k.data