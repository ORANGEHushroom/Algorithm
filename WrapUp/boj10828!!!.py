# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
import sys
n = int(sys.stdin.readline())

stack=[]
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0]=='push':
        stack.append(command[1])
    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])

# 밑 두개 다 시간초과 나옴
#결론적으로 그냥 공백으로 안나눠져도
# 스플릿하고 나눠서하자...
#큰 차이가 왜나는지는 잘모르겟지만...
#뭔가 들어갈때 공백이 같이 잡히나봐

import sys

n = int(sys.stdin.readline())
stack = []
for _ in range(1, n+1):
    n = sys.stdin.readline()
    if len(n) > 5:
        p , a = n.split()
        stack.append(int(a))
    elif n == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
        
    elif n == 'size':
        print(len(stack))
    elif n == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif n == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            a = stack.pop()
            print(a)

# n = int(input())
# stack = []
# for _ in range(1, n+1):
#     n = input()
#     if len(n) > 5:
#         p , a = n.split()
#         stack.append(int(a))
#     elif n == 'top':
#         try:
#             print(stack[-1])
#         except:
#             print(-1)
#     elif n == 'size':
#         print(len(stack))
#     elif n == 'empty':
#         if stack:
#             print(0)
#         else:
#             print(1)
#     elif n == 'pop':
#         try:
#             a = stack.pop()
#             print(a)
#         except:
#             print(-1)
