T = int(input())
for tc in range(1,T+1):
    x,y = map(str,input().split())
    a = ''
    for i in y:
        a+=i*int(x)
    print(a)
