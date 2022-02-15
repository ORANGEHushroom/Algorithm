n = int(input())
li = []
for i in range(1, n+1):
    x, y = map(int,input().split())
    li.append([x,y])
li.sort(key=lambda x: x[0])
li.sort(key=lambda x: x[1])
for i in li:
    print(*i)