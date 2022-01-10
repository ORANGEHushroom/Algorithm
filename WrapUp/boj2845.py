num, size = map(int,input().split())
li = list(map(int,input().split()))
total = num*size
for i in li:
    print(i-total,end=" ")