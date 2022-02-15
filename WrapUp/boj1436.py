# 어떤 수에 6이 적어도 3개이상 연속으로 들어가는 수
n = int(input())
a = 666                             
cnt = 1
while cnt < n:
    a += 1
    if '666' in str(a):
        cnt+=1
    if cnt == n:
        break
print(a)
