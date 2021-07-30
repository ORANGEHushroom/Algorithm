
T = int(input())
 
for tc in range(1, T + 1): 
 
    N = int(input())
 
    number_checked = [False for _ in range(10)]
    count = 0
 
    result = N
 
    while count < 10:
 
        N_str = str(result)
        for n in N_str:
            if not number_checked[int(n)]:
                number_checked[int(n)] = True
                count += 1
         
        if count >= 10:
            break
        result += N
     
    print(f'#{tc} {result}')


       
#sol2
       
T = int(input())
 
test_cases = []
for i in range(T):
    test_cases.append(int(input()))
 
for i, case in enumerate(test_cases, start = 1):
    check_num = []
    num = 0
 
    while len(check_num) <10:
        num += case
        temp = str(num)
        for char in temp:
            if char not in check_num:
                check_num.append(char)
 
    print(f'#{i} {num}')




#sol3)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
     
    multi = int(input())
    all_num = set(range(10))
 
    now_num_collect = set({})
 
 
    start_num = multi
    cnt = 1
 
    while True :
        for num in str(start_num) :
            if int(num) not in now_num_collect :
                now_num_collect.add(int(num))
         
        if now_num_collect == all_num:
            break
         
        cnt += 1
        start_num += multi
         
    print('#{} {}'.format(test_case, start_num))   