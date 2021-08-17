a , y1 = map(int,input().split()) #가로로 슬라이스 0 3
b, x1 = map(int,input().split()) # 세로 슬라이스 1 4 
c, y2 = map(int,input().split()) # 0 2


x, y = map(int, input().split())
garo = [0, x]  # 가로
sero = [0, y]  # 세로
cut_times = int(input())
for i in range(cut_times):
    num, line_num = map(int, input().split())
    if num == 0:  
    # num이 0이면 문제에서 가로로 '자르는' 점선이라 했으므로, 이 선은 엄연히 세로에 속하는 선이다.
        sero.append(line_num)
    else:  
# 반대의 경우도 마찬가지다. 속지 말자.
        garo.append(line_num)

garo = sorted(garo)
sero = sorted(sero)
result_list = []
for i in range(1, len(garo)):
    for j in range(1, len(sero)):
        width = garo[i] - garo[i-1]
        height = sero[j] - sero[j-1]
        result_list.append(width * height)

print(max(result_list))