import sys
sys.stdin=open('1983.txt')

def whatif(k):
    score_range = int(num_student//10) #2라고하면
    if 0 <= k < score_range:  # 0,1
        print('D0')
    elif score_range <= k < score_range*2 :
        print('C-')
    elif score_range*2 <= k < score_range*3:
        print('C0')
    elif score_range*3<= k < score_range*4:
        print('C+')
    elif score_range*4<= k < score_range*5:
        print('B-')
    elif score_range*5<= k < score_range*6:
        print('B0')
    elif score_range*6<= k < score_range*7:
        print('B+')
    elif score_range*7<= k < score_range*8:
        print('A-')
    elif score_range*8<= k < score_range*9:
        print('A0')
    else:
        print('A+')




T = int(input())
for tc in range(1,T+1):
    print('#{}'.format(tc),end=" ")
    num_student, whatscore = map(int,input().split())
    
    li = []
    for j in range(1,num_student+1):
        mid, fin, assign = map(int,input().split())
        li.append([j, mid, fin, assign]) 
        # 순서대로 받으니까 순서포함해서 모든값 넣어
    total = []
    total_fin = []
    for j, mid, fin, assign in li:
        to = mid*0.35 + fin*0.45 +assign*0.2
        total.append([j,to]) # 내순서랑 총점
        total_fin.append(to) #총점만

    total_fin.sort() # 총점을 순서대로 나열

    fina = 0
    for x,y in total: # 아까 위에서 순서랑 총점 담았으니
        if x == whatscore:  # 내가 성적을 원하는 순서라면
            fina = y # 원하는 성적
    alpha = total_fin.index(fina) # 내 성적을 가진 애가 몇등인지 알기
    whatif(alpha) # 몇등이라면 무슨 점수인가
    
    
# grade_list = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     grades = [list(map(int, input().split())) for _ in range(N)]
#     score_list = []
#     for grade in grades:
#         total = (grade[0] * 0.35) + (grade[1] * 0.45) + (grade[2] * 0.2)
#         score_list.append(total)

#     K_score = score_list[K-1]
#     score_list.sort(reverse=True)
#     tmp = N // 10
#     matching_K_grade = score_list.index(K_score) // tmp

#     print('#{} {}'.format(tc, grade_list[matching_K_grade]))