# import sys
# sys.stdin = open('18111.txt')

# sero,garo,given_block = map(int,input().split())

# # 0을 기준으로 다 더한게 n*m의 몇배수인지(그걸구해서 빼면되자나 각 3초씩),
# #  나머지는 다 넣어버릴거고...1초
# land = [list(map(int,input().split())) for _ in range(sero)]
# max_num = []
# min_num = []
# for i in land:
#     max_num.append(max(i))
#     min_num.append(min(i))
# max_num = max(max_num)
# min_num = min(min_num)

# total = 0
# for k in range(sero):
#     for j in range(garo): #카운트 가장 높은 애한테 맞춰야?? 
#         total += abs(min_num - land[k][j]) #1
# basu = total // (sero*garo) #0
# namun = total % (sero*garo) #1
# fin = max_num - basu #1 새로운 고층
# print(basu,namun)
# if total < garo*sero:
#     print(total*2, min_num) #시간 높이  
#     # 작다는 거면... 원래애들에서 나머지뺀거니까... 
# else: # 배수가 0이 아니라면 1이라면 
#     #최대값64에서  1을 깎은 63 fin을 기준으로 
#     total_2 = 0
#     for a in range(sero):
#         for b in range(garo):
#             total_2 += abs(fin - land[a][b])
#     alpha = (total_2-namun)//2
#     print(alpha*3+namun*2,max_num) -> 문제: 인벤토리에서 꺼내는 경우 1초니까
# 그것도 생각하자
    
    
        

import sys

N, M, B = map(int, sys.stdin.readline().split())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
time, height = 9223372036854775807, 0
for h in range(257):
    bot, top = 0, 0
    for i in range(N):
        for j in range(M):
            if li[i][j] < h:
                bot += h - li[i][j]
            else:
                top += li[i][j] - h
    if bot > top + B:
        continue
    t = bot + top * 2
    if t <= time:
        time = t
        height = h
print(time, height)