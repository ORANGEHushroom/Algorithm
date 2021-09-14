import sys
sys.stdin = open('1927.txt')

n = int(input())
a = ['3','6','9']
for i in range(1, n+1):
    b = str(i)
    cnt = 0
    for j in b:
        if j in a:
            cnt+=1
    print('{}'.format('-'*cnt),end=" ")
        
    if '3' not in b and '6' not in b and '9' not in b:
        print(b,end=" ")