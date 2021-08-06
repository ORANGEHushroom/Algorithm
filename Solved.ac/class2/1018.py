x,y = map(int,input().split())

for tc in range(1,y+1):
    a = list(map(str,input().split()))
    for i in range(1,x-6):
        b = a[i:i+8]
        count = 0
        for j in range(len(b)):
            if b[j] == b[j+1]:
                count+=1
    print(count)
    #x가 10일때 b는 2~10까지 슬라이싱 그러면 2:11 범위는 