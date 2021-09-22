import sys
sys.stdin = open('11445.txt')

t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc),end=' ')
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #print(len(a)) #25
    p = input()
    q = input() #동일 자리:1자리라면 알파벳 뒤인지가.. 2자리라면 1자리는 같고 뒤만달라야 ... 마찬가지!
    # 앞이 한자리 적다면.. 1자리고 2자리면? 앞은 z aa 라던가..
    #for i in range(len(p)): # 1 이라면
    # 같은 자리수라면: 앞자리들이 다 같은지 & 맨뒷자리가 하나 차이인지
    if len(p) == len(q):
        if p[:len(p)-1] == q[:len(q)-1] and a.index(p[-1])+1 == a.index(q[-1]):
            print('N')
        else:
            print('Y')
    
    elif len(p) != len(q):     # 다른 자리라면 p의 전체가 q랑 같고.. q의 마지막은 a여야하고.. az az
        if p == q[:len(q)-1] and q[-1] == 'a':
            print('N')
        else:
            print('Y')    


