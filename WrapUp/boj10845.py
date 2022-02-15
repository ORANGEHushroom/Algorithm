"""
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""
import sys
n = int(sys.stdin.readline())
que = []
for _ in range(1, n+1):
    word = sys.stdin.readline().split()
    # 얘를 readline 하면 ['push', '1'] 이케들어감..
    #print(word)
    if word[0] == 'push':
        que.append(int(word[1]))
    if word[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            a = que.pop(0)
            print(a)
    if word[0] == 'size':
        print(len(que))
    if word[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    if word[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    if word[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])