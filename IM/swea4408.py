T = int(input())
for tc in range(1, T+1):
    num = int(input())
    a = []
    for k in range(num):
        a.append(list(map(int,input().split()))) #[[10,20] [30,40]]
    count = 1
    for i in range(len(a)):
        if i+1 <= len(a)-1 and a[i][1] > a[i+1][0]:
            count += 1
    print('#{} {}'.format(tc,count))