T = int(input())
# test case의 횟수만큼 for문을 돌림
for i in range(T):
    
    # test case 번호 입력받음
    n = int(input())
    
    # 점수들 list에 넣음
    scores = list(map(int, input().split()))

    # 가장 많이 나오는 점수를 저장하기 위한 변수
    max = 0
    
    # 입력되는 점수의 갯수는 1000개인데 점수의 범위는 0~100이니까 0~100으로 for문을 돌리는게 더 효율적일 것 같았음
    for score in range(101):

        # 특정 점수가 리스트에 없을 때
        if scores.count(score) == 0:
            continue    # 그냥 다음 점수로 넘어가자

        # 특정 점수가 #개 있고, 그게 현재 최빈수보다 크면 keep
        elif scores.count(score) > scores.count(max):
            max = score

        # 특정 점수가 #개 있는데 현재 최빈수의 갯수랑 똑같으면 더 큰 점수를 keep
        elif scores.count(score) == scores.count(max):
            if score>max:
                max = score
    
    # 최빈수 출력
    print(f"#{n} {max}")

#다른 풀이법

T = int(input())

for Test in range(T):
    A = int(input())
    arr = list(map(int,input().split()))
    People = [0]*101 #people = [0 for _ in range(101)] 추천 0을 101번 반복
    ans = 0
    a = 0
    count = 0
    for Score in arr:
        for i in range(101):
            if i == Score:
                People[i] += 1
    for k in People:
        if a <= k:
            ans = count
            a = k
        count += 1
    print(f'#{Test+1} {ans}')