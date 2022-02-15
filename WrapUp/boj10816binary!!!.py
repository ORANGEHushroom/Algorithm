import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

A.sort()

# lower bound와 upper bound 함수를 따로 만들어도 되지만,
# 편의상 인자로 기능을 달리하게끔 했다.
def bs(num, bound):
    start, end = 0, n
    while(start < end):
        mid = (start + end) // 2
        if bound == 0:
            if A[mid] < num:
                start = mid + 1
            else:
                end = mid
        else:
            if A[mid] <= num:
                start = mid + 1
            else:
                end = mid
    return end

result = []
for i in B:
    result.append(bs(i,1) - bs(i,0))
print(*result)

from collections import Counter
from sys import stdin

n = stdin.readline().rstrip()
card = list(map(int,stdin.readline().split()))
m = stdin.readline().rstrip()
test = list(map(int,stdin.readline().split()))

count = Counter(card)

for i in range(len(test)):
    if test[i] in count:
        print(count[test[i]], end=' ')
    else:
        print(0, end=' ')


#아래 방식은 시간초과남
# 이진탐색을 쓰던가
# 카운터로 딕셔너리로 만들어야...



import sys

n = sys.stdin.readline()
cnt = list(sys.stdin.readline().split())
m = int(sys.stdin.readline())
li = list(sys.stdin.readline().split())
result = [0] * m
for i in range(len(li)):
    result[i] = cnt.count(li[i])
print(*result)
