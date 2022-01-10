#나중에 다시풀어보기

t = int(input()) 
for tc in range(1, t+1):
    n = int(input())
    li = list(map(int,input().split()))
    sell = 0
    cnt = 0
    profit = 0
    for i in range(n-1):
        if li[i] <= li[i+1]:
            sell += li[i]
            cnt += 1
            if i+1 == n-1:
                profit += li[i+1] * cnt - sell
                break
        elif li[i] > li[i+1]:
            profit += li[i] * cnt - sell
    print(f'#{tc} {profit}')

T = int(input())
for t in range(1,T+1):
    num = int(input())
    arr = list(map(int,input().split()))
    #배열을 뒤집음
    arr = arr[::-1]
    #첫 원소를 최대값으로 저장
    max_v = arr[0]
    cnt = 0
    for i in range(1,len(arr)):
        #최대값보다 작은 값이면 이득을 본 것으로 계산
        if max_v > arr[i]:
            cnt += max_v-arr[i]
        #최대값보다 더 큰 값이면 새로운 최대값으로 저장
        else:
            max_v = arr[i]
    print("#{} {}".format(t, cnt))