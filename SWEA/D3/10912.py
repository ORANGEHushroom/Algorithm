import sys
sys.stdin = open('10912.txt')

t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc), end=" ")
    li = list(map(str,input()))
    li.sort() # aaabbbcccb 
    fin = []
    while len(li) > 1: 
        a = li.pop(0)
        b = li.pop(0)
        if a == b:
            continue
        else:
            fin.append(a)
            li.insert(0,b) # 앞으로 들어가도록

    if len(li) == 1:
        fin = fin + li
    if len(fin) == 0:
        print('Good')
    else:
        fin.sort()
        a = ""
        for i in range(len(fin)):
            a+=fin[i]
        print(a)
