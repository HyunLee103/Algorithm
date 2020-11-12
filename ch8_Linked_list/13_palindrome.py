import collections
from linked_list import Node


head = Node(None)
node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(1)
tail = Node(None)
head.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = tail


# My
def isPalin(input):
    lst = []
    while input is not None:
        lst.append(input.data)
        input = input.next

    while len(lst) > 1:
        if lst.pop() != lst.pop(0):
            return False
    
    return True

isPalin(head)

"""
처음엔 리스트로 풀었는데, 파이썬 리스트는 동적배열이라 list.pop(0), 즉 리스트에
맨 앞 요소롤 꺼내오는 작업을 하면 전체 리스트를 한칸씩 shift 해야되서 O(n) 소요
따라서 이중 연결 리스트인 Deque 사용하는게 .pop(0) 연산에 효과적 - O(1) 

Deque는 파이썬에서 stack과 queue 기능을 모두 가진 객체
"""
# Deque
def isPalin(head):
    Deque = collections.deque()
    while head is not None:
        Deque.append(head.data)
        head.next
    
    while len(Deque) > 1:
        if Deque.popleft() != Deque.pop():
            return False
    
    return True


# Runner
l1 = ListNode()

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        node = head
        list_tmp = []
        
        if node == False : # 빈 linked list이면 팰린드롬이므로 True반환
            return True
        
        while node is not None : #linked list를 list로 변환
            list_tmp.append(node.val) 
            head = node.next
        
        # print(type(list_tmp)) -> "list"
        
        if list_tmp == list_tmp[::-1]: #팰린드롬 확인
            return True
        else :
            return False


