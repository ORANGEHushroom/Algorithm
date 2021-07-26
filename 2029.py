T = int(input())

for test_case in range(1, T + 1):
    a,b =map(int,input().split())
    n,m = divmod(a,b)
    print(f'#{test_case} {n} {m}')
