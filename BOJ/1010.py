from itertools import combinations
import sys
sys.stdin = open('1010.txt')


# 시간 초과!
# t = int(input())
# for tc in range(1, t+1):
#     n,m = map(int,input().split())
#     print(len(list(combinations(range(1,m+1),n))))
    

T = int(input())

for _ in range(T):
    m, n = map(int, input().split())
    answer = 1
    k = n - m
    
    while n > k:
        answer *= n
        n -= 1
    while m > 1:
        answer = answer // m
        m -= 1
    
    print(answer)
