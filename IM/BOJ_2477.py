## 미완

import sys
sys.stdin = open('input_fruit.txt')

# N = int(input())
# li = []
# for _ in range(6):
#     x,y = map(int,input().split())
#     li.append([x,y])
# #print(li) #[(4, 50), (2, 160), (3, 30), (1, 60), (3, 20), (1, 100)]


# # li_1 = []
# # li_2 = []
# # li_3 = []
# # li_4 = []
# total = {1:0, 2:0, 3:0, 4:0}
# for i in range(6):
#     if li[i][0] == 1:
#         # li_1.append(li[i][1])
#         total[1] += 1
#     elif li[i][0] == 2:
#         # li_2.append(li[i][1])
#         total[2] += 1
#     elif li[i][0] == 3:
#         # li_3.append(li[i][1])
#         total[3] += 1
#     elif li[i][0] == 4:
#         # li_4.append(li[i][1])
#         total[4] += 1
# # print(total) {1: 2, 2: 1, 3: 2, 4: 1}
# num2 = []
# for key, value in total.items():
#     if value == 2:
#         num2.append(key) 
# # print(num2) [1,3]
# num3 = []
# for x, y in li:
#     if x in num2:
#         pass
    


melon = int(input()) # 참외 개수 K
values = [input().split() for _ in range(6)] # 나머지 2~7 line의 6 줄을 입력 받는다.
directions = [int(v[0]) for v in values] # 방향을 뽑아내서 저장한다.
lengths = [int(v[1]) for v in values] # 길이를 뽑아내서 저장한다.
max_lengths, box_lengths = [], [] # 큰 박스의 길이, 작은 박스의 길이를 담을 배열

for i in range(1, 5): # 방향들 
    if directions.count(i) == 1: # direction이 한번만 존재한다 == 큰 박스의 변
        max_lengths.append(lengths[directions.index(i)]) # 큰박스의 변 길이 저장
        temp = directions.index(i) + 3 # 큰 박스 + 3 == 작은 박스의 변
        if temp >= 6:
            temp -= 6 # cycle을 위해 6 이상일 경우 -6
        box_lengths.append(lengths[temp]) 

area = max_lengths[0] * max_lengths[1] - box_lengths[0] * box_lengths[1]
print(melon * area)