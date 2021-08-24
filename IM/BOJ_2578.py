# 미완인 코드... 
player = [list(map(int, input().split())) for _ in range(5)] # 철수꺼
dir = [list(map(int, input().split())) for _ in range(5)] #지휘자꺼
li = [[0]*5 for _ in range(5)] # 0으로된 빈 배열

result = []
for i in range(5):
    for j in range(5):
        result.append(dir[i][j])  # 리스트 안에 지휘자가 불러주는 번호들 순서대로 정리
print(result)
count = 0 # 몇번째 불러주는 수인지 세자
for i in result:
    for a in range(5):
        for b in range(5):
            if player[a][b] == i: # 지휘자가 불러주는 숫자가 철수의 몇번인지
                li[a][b] = 1 # 철수의 위치랑 동일한 좌표로 빈 배열에 체크
                count += 1 # 숫자하나더하기
                row = 0 
                col = 0
                v1 = 0
                v2 = 0
                for x in range(5):
                    for y in range(5):
                        v1 += li[x][x] #대각선의 합
                        v2 += li[4-x][4-x] #반대대각선
                if v1 == 5 or v2 == 5 or row ==5 or col ==5: #합이 5가되면..
                    break
                print(count) # 하다가 일단 스탑
    



                        
                
