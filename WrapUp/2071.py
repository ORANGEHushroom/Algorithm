t = int(input())
for tc in range(1, t+1):
    num = list(map(int, input().split()))
    total = sum(num)
    result = round(total / 10)
    print(f'#{tc} {result}')