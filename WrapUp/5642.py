t = int(input())
for tc in range(1,t+1):
    n = int(input())
    li = list(map(int,input().split()))
    
    a = len(li)
    cnt = 0
    fin = []
    while cnt < len(li):
        cnt += 1
        result = []
        for i in range(0,len(li)-cnt+1):
            result.append(sum(li[i:i+cnt]))
        a = max(result)
        fin.append(a)
    print(f'#{tc} {max(fin)}')