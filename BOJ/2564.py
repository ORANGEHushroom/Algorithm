import sys
read = sys.stdin.readline

def get_distance(x, y):
    if x == 1:  # 북
        return y
    if x == 2:  # 남
        return w + h + w - y
    if x == 3:  # 서
        return w + h + w + h - y
    if x == 4:  # 동
        return w + y

# 입력
w, h = map(int, read().split())
n = int(read())

# 풀이
course = []
for _ in range(n + 1):  # (0, 0) 에서 상점까지의 거리
    x, y = map(int, input().split())
    course.append(get_distance(x, y))

answer = 0

for i in range(n):  # 동근이와 상점 사이의 최단거리
    in_course = abs(course[-1] - course[i])
    out_course = 2 * (w + h) - in_course
    answer += min(in_course, out_course)

# 출력
print(answer)



# # 경비원
# import sys
# sys.stdin = open('2564.txt')

# garo, sero = map(int,input().split())
# num_shop = int(input())
# dic = []
# for _ in range(num_shop):
#     dic.append(list(map(int,input().split())))
# #print(dic) # [[1, 4], [3, 2], [2, 8]]

# x, y = map(int,input().split())
# total = []
# for i in dic:
#     dir = i[0]
#     point = i[1]
#     if dir == x:
#         total.append(abs(point-y))
#     elif dir != x: # 같은 변 아님
#         if x%2 : # 홀수
#             if dir % 2:
#                 total.append(abs(min(sero+point+y, sero+garo-point+garo-y)))
#             else: # 짝수
#                 if x == 3:
#                     if dir == 2:
#                         total.append(abs(y+point))
#                     elif dir == 4:
#                         total.append(abs(garo-y+point))
#                 elif x == 1:
#                     if dir == 2:
#                         total.append(abs(y+garo-point))
#                     elif dir == 4:
#                         total.append(abs(garo-y+garo-point))
#         elif x % 2 == 0: #짝수
#             if dir % 2 == 0:
#                 total.append(abs(min(garo+point+y, garo+sero-point+sero-y)))
#             else:
#                 if x == 2:
#                     if dir == 3:
#                         total.append(abs(sero-y+point))
#                     elif dir == 1:
#                         total.append((sero-y+point))
#                 elif x == 4:
#                     if dir == 2:
#                         total.append(abs(y+sero-point))
#                     elif dir == 1:
#                         total.append(abs(sero-y+sero-point))
# print(total)
