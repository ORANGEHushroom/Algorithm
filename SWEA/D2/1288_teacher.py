#강사님 솔루션
T = int(input())
 
for tc in range(1, T + 1): 

    N = int(input())
    count = 1
    #리스트에 인덱스를 붙이기 위해 체크리스트, 숫자가 나오면 1로 바꾸자
    check = [0 for _ in range(10)] # =[0,0,0,0,0,0,0,0,0,0]
    # 1. 주어진 N을 증가시킨다.
    #1N 2N 3N....
    #2.각 회차에서 나오는 수를 분리한다.
    #EX) 1235-> 1 2 3 4로 나눠서 보기 1234 => '1234'
    #3. 위에서 나눈 숫자 체크하기
    result = None
    while True:
        number = str(N * count)
        for num in number:                            
            idx = int(num) #num을 인덱스로 활용해서 체크
            check[idx] = 1 #얘는지금 str이니까 int로 변환
        #다음으로 가기 전에 다 체크했는지 확인
        #체크 배열의 전체가 1로 표기되었는지 확인
        is_all_checked = True
        for i in check: #0,1,1,..(인덱스가 아니라 실제값)
            if i == 0:
                is_all_checked = False # 0이 나오는순간 거짓으로바꿔
                break #아직 완료아니니까
        if is_all_checked:
            result = number
            break #모든 리스트의 요소가 1로ㅗ 채워져있음 while종료
        count += 1  
    
    print(f'#{tc} {result}')
    #4. 0~9까지 다 체크했으면 종료하기
    #그리고 그때의 회차를 정답으로 프린트
