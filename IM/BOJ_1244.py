switch = int(input()) #스위치 개수

list_status = list(map(int,input().split())) #스위치 초기상태

num_students = int(input()) #학생수

for i in range(num_students):

    gender, student_switch = map(int,input().split()) #성별, 받은수

    if gender == 1: #남자라면 배수 구해야하니까 스위치 수를 받은 수로 나눠서 범위 만듬
        for i in range(1, (len(list_status) // student_switch) + 1):
            if list_status[(student_switch * i) - 1] == 0: #배수의 위치의 숫자가 0이면
                list_status[(student_switch * i) - 1] = 1 #1로 만들어
            else:
                list_status[(student_switch * i) - 1] = 0 #반대의 경우 0으로

    if gender == 2: #여자라면 
        # 인덱스가 0부터 시작하니까 받은 수의 위치를 구하기 위해 -1 
        # =>받은 수 위치의 값이 0이라면
        if list_status[(student_switch - 1)] == 0: 
            list_status[(student_switch - 1)] = 1 #1로만들어
        else:
            list_status[(student_switch - 1)] = 0
        l = student_switch - 2 #받은수에서 2뺀값(받은수위치값이 -1이니까,,)
        r = student_switch #그대로 받은수 
        #엘이 0보다 크며 r이 스위치범위를 안넘으면서 l과r의 값이 동일할때까지
        while l >= 0 and r < switch and list_status[l] == list_status[r]:
            if list_status[l] == 0: #0이면
                list_status[l], list_status[r] = 1, 1 #둘다 1로
            elif list_status[l] == 1: #1이면
                list_status[l], list_status[r] = 0, 0 #0으로
            l -= 1 #범위 늘리기위해 하나씩 빼고 더하고
            r += 1
            if l < 0 or r >= switch: #범위를 넘으면 스탑
                break

for i in range(1,len(list_status)+1): #20개씩 끊어내기위해,,인덱스0따로빠질까봐 1부터
    print(list_status[i-1], end=" ") #1부터 시작햇으니 범위 넘을까봐 -1
    if i % 20 == 0:
        print() #20개마다 프린트하기위해 


        
# cnt = 0
# result = ''
# for i in range(switch):
#     result += (str(list_status[i]) + ' ')
#     cnt += 1
#     if cnt == 20:
#         print(result)
#         result = ''
#         cnt = 0
# if len(result) != 0:
#     print(result)

