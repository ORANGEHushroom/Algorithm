import sys
from collections import Counter

sys.stdin=open('1204.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    total = []
    li = list(map(int,input().split()))
    for i in li:
        total.append((i,li.count(i))) # 숫자. 그 숫자의 개수
    num = []
    for j in li:
        num.append(li.count(j)) # 숫자들의 개수
    max_num = max(num) #가장 많이 몇번 나오는지 그 값을 구함 
    fin = []
    for x,y in total:
        if y == max_num:
            fin.append(x)
    print('#{} {}'.format(tc,max(fin)))


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    li = list(map(int,input().split()))
    a = Counter(li)
    vli = []
    for value in a.values():
        vli.append(value)
    max_va = max(vli)
    total = []
    for key, value in a.items():
        if value == max_va:
            total.append(key)
    print('#{} {}'.format(tc,max(total)))
