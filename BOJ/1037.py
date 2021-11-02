num = int(input())
li = list(map(int,input().split()))
li.sort()
if len(li) == 1:
    total = li[0]**2
else:
    total = li[0]*li[-1]

print(total)
