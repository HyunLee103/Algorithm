from linked_list import Node

# head1 = Node(None)
lst_node1 = Node(2)
node_2 = Node(4)
node_3 = Node(3)
# tail = Node(None)
# head1.next = node_1
lst_node1.next = node_2
node_2.next = node_3
# node_3.next = tail

# head2 = Node(None)
lst_node2 = Node(5)
node_2 = Node(6)
node_3 = Node(4)
# tail = Node(None)
# head2.next = node_1
lst_node2.next = node_2
node_2.next = node_3
# node_3.next = tail


# my
def sum_twolist(l1,l2):
    lst1, lst2 = [], []

    while l1:
        value = l1.data
        lst1.append(value)
        l1 = l1.next
    while l2:
        value = l2.data
        lst2.append(value)
        l2 = l2.next

    print(lst1,lst2)
    lst1.reverse()
    lst2.reverse()

    return int(''.join(map(str,lst1))) + int(''.join(map(str,lst2))) # 숫자형 리스트는 문자형 리스트로 바꿔야 join 가능


# 몫과 나머지 이용
def sum_towlist2(l1,l2):
    root = head = Node(0)

    carry = 0
    while l1 and l2:
        sum = 0

        sum += l1.data
        l1 = l1.next
        sum += l2.data
        l2 = l2.next

        carry, res = divmod(sum+carry,10)
        head.next = Node(res)
        head = head.next

    return root.next

if __name__ == "__main__":
    sum_twolist(lst_node1,lst_node2)
    res_linkedlist = sum_towlist2(lst_node1,lst_node2)
