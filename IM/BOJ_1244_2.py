num_switch = int(input())
li = list(map(int, input().split()))
num_student = int(input())
for _ in range(num_student):
    gender, number = map(int, input().split())
    if gender == 1:
        for i in range(1, num_switch+1):
            if i % number == 0:
                if li[i-1] == 1:
                    li[i-1] = 0
                elif li[i-1] == 0:
                    li[i-1] = 1
    elif gender == 2:
        k = min(number-1, num_switch - number) #2
        j = 0
        while j <= k: #0 1 2
            if li[number+j-1] == 0 and li[number-j-1] == 0:
                li[number+j-1] = 1
                li[number-j-1] = 1
                j+=1
            elif li[number+j-1] == 1 and  li[number-j-1] == 1:
                li[number+j-1] = 0
                li[number-j-1] = 0
                j+=1  
            
            else:
                break


for r in range(1, len(li)+1):
    if r % 20 == 1 and r+19 < len(li):
        print(*li[r-1:r+19])  #0~19 0~20
    elif r % 20 == 1 and r+19 >= len(li):
        print(*li[r-1::])

# for i in range(0,len(switch),20):
#     print(*switch[i:i+20])
    



# for i in range(1,len(li)+1): #20개씩 끊어내기위해,,인덱스0따로빠질까봐 1부터
#     print(li[i-1], end=" ") #1부터 시작햇으니 범위 넘을까봐 -1
#     if i % 20 == 0:
#         print() #20개마다 프린트하기위해 
