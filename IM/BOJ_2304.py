N = int(input())
max_height = 0
max_idx = 0
max_length = 0
total = 0
roof = []
for _ in range(N):
    L, H = map(int, input().split()) [2, 8]
    roof.append([L, H])
    if H > max_height:
        max_height = H
        max_idx = L
    if L > max_length:
        max_length = L
total_list = [0] * (max_length + 1)
for m, n in roof:
    total_list[m] = n
left = 0
right = 0
for i in range(max_idx+1):
    if total_list[i] > left:
        left = total_list[i]
    total += left
for j in range(max_length, max_idx, -1):
    if right < total_list[j]:
        right = total_list[j]
    total += right
print(total)




# 미완인 코드!

# N = int(input())
# lines = {}
# for _ in range(N):
#     idx, height = map(int,input().split())
#     lines[idx] = height #딕셔너리 

# tall = max(lines.values()) #제일 높은 블럭
# idx_min = min(lines.keys()) #박스의 시작
# idx_max = max(lines.keys()) #박스의 끝

# size = (idx_max - idx_min +1) * tall #전체크기
# print(size)
# for key,value in lines.items():
#     if value == tall:
#         main_idx = key #제일 키큰 애의 위치
# # 전체 크기에서 제일작은애랑 큰애랑 키큰애차를 빼서... 
# size_a = size-(main_idx-idx_min)*(tall - lines[idx_min]) -(idx_max-main_idx)*(tall-lines[idx_max])
    
# for i in range(main_idx): #i = 4
#     if i in lines.keys() and lines[idx_min] < lines[i] < tall: # 내 왼쪽이 나보다 작아야하고 오른쪽에는 
#         size_a += (main_idx-i)*(lines[i]-lines[idx_min])
#     else:
#         continue # 일단 여기까지...하다가...ㅌㅌ


# 스택풀이
# N = int(input())
# wall_list = [0] * 1001
# max_h = 0
# max_h_idx = 0
# end_idx = 0
# for _ in range(N):
#     idx, h = map(int, input().split())
#     wall_list[idx] = h
#     if max_h < h:
#         max_h = h
#         max_h_idx = idx
#     end_idx = max(end_idx, idx)

# answer = 0
# stack = []
# for i in range(0, max_h_idx+1):
#     if not stack:
#         stack.append(wall_list[i])
#         answer += stack[-1]
#     else:
#         if stack[-1] < wall_list[i]:
#             stack.pop()
#             stack.append(wall_list[i])
#         answer += stack[-1]

# stack = []
# for i in range(end_idx, max_h_idx, -1):
#     if not stack:
#         stack.append(wall_list[i])
#         answer += stack[-1]
#     else:
#         if stack[-1] < wall_list[i]:
#             stack.pop()
#             stack.append(wall_list[i])
#         answer += stack[-1]

# print(answer)

#sol2
# N = int(input())
# min_L = 1000
# max_L = 1
# max_H_idx = -1
# max_H_val = -1
# input_list = []

# # 입력 정보 확인
# for _ in range(N):
#     L, H = map(int, input().split())
#     input_list.append((L, H))
#     if L < min_L:
#         min_L = L
#     if L > max_L:
#         max_L = L
#     if H > max_H_val:
#         max_H_val = H
#         max_H_idx = L

# # 기둥 높이 리스트
# my_list = [0] * (max_L + 1)
# for L, H in input_list:
#     my_list[L] = H

# # 왼쪽부터 top까지 탐색
# temp = 0
# my_sum = 0
# for i in range(max_H_idx + 1):
#     if my_list[i] > temp:
#         temp = my_list[i]
#     my_sum += temp

# # 오른쪽부터 top까지 탐색
# temp = 0
# for j in range(max_L, max_H_idx, -1):
#     if my_list[j] > temp:
#         temp = my_list[j]
#     my_sum += temp

# print(my_sum)