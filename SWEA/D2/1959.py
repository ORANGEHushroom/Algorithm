T = int(input())
for test_case in range(1,T+1):
    answer = 0
    N, M = map(int,input().split())
    list_n = list(map(int,input().split()))
    list_m = list(map(int,input().split()))
    max_total = 0
    if N > M:
        for i in range(N-M+1):
            temp_total = 0
            for j in range(M):
                temp_total += list_n[j+i] * list_m[j]
            if temp_total > max_total:
                max_total = temp_total
    elif N < M:
        for i in range(M-N+1):
            temp_total = 0
            for j in range(N):
                pass
                temp_total += list_n[j] * list_m[j+i]
            if temp_total > max_total:
                max_total = temp_total
    else :
        for i in range(N):
            max_total += list_n[i] * list_m[i]
    answer = max_total
     
    print(f'#{test_case} {answer}')