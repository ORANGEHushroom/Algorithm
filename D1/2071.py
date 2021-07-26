T = int(input())
for test_case in range(1, T + 1):

    a = sum(map(int,input().split()))
    result = int(round(a/10))
    print(f'#{test_case} {result}')