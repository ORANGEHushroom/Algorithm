#시간 초과난 내 풀이
import sys
a,b,v = map(int,sys.stdin.readline().split())
day = 0
while True:
    day+=1
    if a*day-b*(day-1) >= v:
        print(day)
        break
    
# a, b, v = map(int, input().split())
# ls = 0
# if (v - b) % (a - b) != 0:
#     ls = ((v - b) // (a - b)) + 1
# else:
#     ls = ((v - b) // (a - b))
# print(ls)

#math 모듈을 이용하면 수학과 관련된 함수들을 사용할 수 있다. 
# ceil 함수를 이용하면 소수를 올림 하는 정수를 반환하고 반대로 소수를 내림한 정수를 반환할 때는 floor를 이용한다. 
#ceil은 천장, floor는 바닥을 의미한다고 생각하면 기억하기가 쉽다.
