T = int(input())
#다른풀이도 참고할것
# T = int(input())
# for i in range(T): 
#     n = int(input())
    
#     scores = list(map(int, input().split()))
#     max = 0
    
#     for score in range(101):    
#         if scores.count(score) == 0:
#             continue    
#         elif scores.count(score) > scores.count(max):
#             max = score
#         elif scores.count(score) == scores.count(max):
#             if score>max:
#                 max = score
#     print(f"#{n} {max}")



for tc in range(1, T+1):
    num = int(input())
    li = list(map(int,input().split()))
    li.sort()
    score = [0] * 101
    for i in li:
        score[i] += 1
    
    maxnum = max(score)
    n = 0
    for i in range(len(score)):
        if score[i] == maxnum:
            n = i
    print(f'#{tc} {n}')
