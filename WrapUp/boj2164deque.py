from collections import deque
#에라이
n = int(input())
deq = deque([i for i in range(1, n+1)])
while len(deq) > 1:
    deq.popleft()               # 제일 왼쪽값 추출 및 삭제
    deq.append(deq.popleft())   # 맨 끝에 값 추가
print(deq.pop()) 


#n = int(input())
#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
#1 2 2 4 2 4 6 8               12 14 16

#if n == 1:
#    print(1)
#elif n == 2:
#    print(2)
#else:
    #시간초과난 sol2)
    #for i in range(2,n):
    #    if n > 2**(i-1) and n < 2**(i):
    #        print(2**i - (2**i - n)*2)
    #    elif n == 2**i:
    #        print(n)

    # 시간초과난 내 sol1
    #stack = []
    #for i in range(2,n+1):
    #    stack.append(i)
    #
    #while len(stack) > 1:
    #    stack.append(stack.pop(0))
    #    stack.pop(0)
    #    
    #print(*stack)
    
    
