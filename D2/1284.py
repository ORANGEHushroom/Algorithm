T = int(input())
for test_case in range(1, T + 1):
    a = list(map(int,input().split()))
    basemoney_A = a[0]
    basemoney_B = a[1]
    below_Rwater = a[2]
    below_Rmoney = a[3]
    spent_water = a[4]


    money1 = basemoney_A*spent_water #실사용 a4
    if spent_water<=below_Rwater:
        money2 = basemoney_B
    else:
        money2 = basemoney_B+below_Rmoney*(spent_water-below_Rwater)

    if money1 > money2:
        print(f'#{test_case} {money2}')
    else:
        print(f'#{test_case} {money1}')

#다른풀이
T = int(input())

# tc만큰 for문 돌리기
for tc in range(1, T+1):
    
    # 각 input을 map으로 받는다
    P, Q, R, S, W = map(int, input().split())

    # A = 사용량 * P원
    A = W*P

    # B = R리터 보다 사용량이 적으면 Q원, R리터 보다 사용량이 높으면 Q원 + 초과량*S
    B = Q if W<R else Q+(W-R)*S

    print("#{} {}".format(tc, A if A<B else B))