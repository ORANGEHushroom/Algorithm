import sys
sys.stdin = open('input.txt')
#오랜만에 보는 딕셔너리니까..
t = int(input()) 
#1/31, 2/28, 3/31, 4/30, 5/31, 6/30, 7/31, 8/31, 9/30, 10/31, 11/30, 12/31
cal = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
for tc in range(1, t+1):
    m1, d1, m2, d2 = map(int, input().split())
    result = 0
    if m1 == m2:
        result = result + d2 - d1 + 1 
    else:
        for i in range(m2-1, m1-1, -1):
            for a , b in cal.items():
                if i == a:
                    result += b 
        result = result + d2 - d1 + 1 
    print(f'#{tc} {result}')
