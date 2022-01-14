import itertools
cnt, num = map(int,input().split())
li = list(map(int,input().split()))

c = itertools.combinations(li,3)

mi = 987654321
for i in c:
    if num >= sum(i) and num - sum(i) < mi:
        mi = num - sum(i)
print(num-mi)
# 이렇게도 가능
a,b = map(int,input().split())
arr = list(map(int,input().split()))
result = 0
for i in range(a):
    for j in range(i+1,a):
        for k in range(j+1,a):
            if arr[i]+arr[j]+arr[k] > b:
                continue
            else:
                result = max(result,arr[i]+arr[j]+arr[k])
print(result)