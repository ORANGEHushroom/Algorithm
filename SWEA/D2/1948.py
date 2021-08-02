T = int(input())
for test_case in range(1,T+1):
    mon1, day1, mon2, day2 = map(int,input().split())
    day = [0,31,28,31,30,31,30,31,31,30,31,30,31]
 
    for i in range(mon1):
        day1 += day[i]
    for i in range(mon2):
        day2 += day[i]
     
    print(f'#{test_case} {day2-day1+1}')
# sol2)
# def day_365(month, day) :
#     mon = 1
 
#     while mon != month+1 :
 
#         if mon in [2, 4, 6, 8, 9, 11] :
#             day += 31
#         elif mon == 3 :
#             day += 28
#         elif mon in [5, 7, 10, 12] :
#             day += 30
         
#         mon += 1
 
#     return day
 
 
# T = int(input())
 
# for t in range(1, T+1) :
#     month1, day1, month2, day2 = map(int, input().split())
     
#     day1 = day_365(month1, day1)
#     day2 = day_365(month2, day2)
 
#     print(f'#{t} {day2 - day1 + 1}')