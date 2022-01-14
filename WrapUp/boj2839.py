n = int(input())
#3을빼서 5의베수로만들기..
# 5로 나눠서 1이 넘으면 3을 빼서 5로 만들수잇는지 확인?
## 일단 가장 먼저 3과 5의 조합으로 다 나눠지는지를 검증
##안되는거 1 2 4 7 
if n in [1, 2, 4, 7]:
    print(-1)
else:
    a = n // 5
    cnt = 0
    for i in range(a,-1,-1):
        n = n - i*5
        if n % 3 == 0:
            cnt += (n // 3)
            cnt += i
            break
        n = n + i*5
    print(cnt)
