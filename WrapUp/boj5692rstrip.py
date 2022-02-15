import sys
##rstrip 안쓰면 시간초과남..
while True:
    n = sys.stdin.readline().rstrip()
    if n == '0':
        break
    else:
        result = 0
        for i in range(1,len(n)+1):
            a = int(n[i-1])
            if a == 0:
                continue
            else:
                for j in range(len(n)-i+1,0,-1):
                    a = a*j
            
            result += a
        print(result)



