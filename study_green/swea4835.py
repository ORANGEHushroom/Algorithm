import sys
sys.stdin = open('input_sum.txt')
# min max 안쓰기
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    result = []
    for i in range(len(li)):
        a = li[i:i+M]
        if len(a) == M:
            b = sum(a)
            result.append(b)        
    max_num = result[0]
    for i in result:
        if i > max_num:
            max_num = i
    min_num = result[0]
    for j in result:
        if j < min_num:
            min_num = j
    print('#{} {}'.format(tc, max_num-min_num))