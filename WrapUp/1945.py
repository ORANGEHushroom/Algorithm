t = int(input()) 
for tc in range(1, t+1):
    print(f'#{tc}',end=" ")
    n = int(input())
    li = [2,3,5,7,11]
    total = [0] * 5
    
    for i in range(len(li)):
        while n % li[i] == 0:
            total[i] += 1
            n = n/li[i]
        
    for i in total:
        print(i,end=" ")
    print()