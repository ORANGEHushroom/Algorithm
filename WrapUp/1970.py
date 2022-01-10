t = int(input()) 
for tc in range(1, t+1):
    n = int(input())
    li = [50000,10000,5000,1000,500,100, 50,10]
    result = [0] * 8
    for i in range(len(li)):
        if n // li[i] >= 1:
            result[i] = n // li[i]
            n %= li[i]
    print(f'#{tc}')
    print(*result)