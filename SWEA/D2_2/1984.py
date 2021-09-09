import sys
sys.stdin=open('1984.txt')

T = int(input())
for tc in range(1, T+1):
    li = list(map(int, input().split()))
    max_num = max(li) #최대
    min_num = min(li) #최소
    total = round((sum(li)-max_num-min_num)/8) #총점에서 빼고 나누기

    print('#{} {}'.format(tc,total))