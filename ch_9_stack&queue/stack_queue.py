"""
스택과 큐는 추상 자료형(ADT) 
stack : 보통 연결 리스트로 구현 -> push/pop 두 기능을 가진 모든 소프트웨어에 사용되는 자료구조, LIFO 
queue : 보통 배열로 구현 -> 우선순위 큐, BFS, 캐시 등 구현할 때 사용, FIFO

둘 다 파이썬 리스트로 구현할 수 있으나, 큐와 같은 경우 맨 앞 요소를 pop하는 연산이 
리스트에서 O(n) 이므로, 이중 연결 리스트인 deque를 사용하는게 좋다.
"""



"""
20. 괄호로 된 입력값이 올바른지 판단
"""
from collections import deque

input = "[](){}"

def valid_paren(input):
    stack = deque(input)
    table = {'(' : ')', '{':'}','[':']'}

    front = []
    back =[]

    for i,s in enumerate(stack):
        if i%2 ==0:
            front.append(table[s])
        else:
            back.append(s)

    if front == back:
        return True
    else:
        return False

valid_paren("[](){}{}")

"""
21. 중복 문자 제외하고 사전 순서로 나열 - Remove duplicate letters
"""




"""
22. 매일 온도를 입력받아, 해당 날보다 따뜻한 날까지 며칠 기다려하는지 출력 - leet code 739
"""

T = [73,74,75,71,69,72,76,73]  

def daily_tem(tem):
    answer = [0] * len(tem)
    stack = []

    for i,t in enumerate(tem):
        while stack and t > tem[stack[-1]]:
            last = stack.pop() # stack에 저장된 마지막 index -> last
                               # pop 되면 해당 값은 stack에서 빠진다 -> 즉 온도가 높아지면 stack에서 제거하고 answer값을 return
            answer[last] = i - last
        stack.append(i)

    return answer

daily_tem(T)