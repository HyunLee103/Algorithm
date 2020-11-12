from linked_list import Node

head1 = Node(None)
node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(4)
tail = Node(None)
head1.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = tail

head2 = Node(None)
node_1 = Node(1)
node_2 = Node(3)
node_3 = Node(4)
tail = Node(None)
head2.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = tail

def mergeTwolist(l1, l2):
    if (not l1) or (l2 and (l1.data > l2.data)):
        l1, l2 = l2, l1 
    if l1:
        l1.next = mergeTwolist(l1.next,l2)