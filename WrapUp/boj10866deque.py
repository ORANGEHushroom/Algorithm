"""
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""

from collections import deque
import sys
sys.stdin = open('input.txt')
n = int(sys.stdin.readline())
##이케 따로 받는것, 메소드들 중요,,
#스택 두개로 한사람도잇넹..ㅎㄷ
dq = deque()
for _ in range(1, n+1):
    word = sys.stdin.readline().split()
    
    if word[0] == 'push_front':
        dq.appendleft(word[1])
    if word[0] == 'push_back':
        dq.append(word[1])

    if word[0] == 'pop_front':
        if len(dq) == 0:
            print(-1)
        else:
            a = dq.popleft()
            print(a)

    if word[0] == 'pop_back':
        if len(dq) == 0:
            print(-1)
        else:
            a = dq.pop()
            print(a)

    if word[0] == 'size':
        print(len(dq))

    if word[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)

    if word[0] == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    if word[0] == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])

