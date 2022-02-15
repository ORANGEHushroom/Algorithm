#시간제한 때매 nlogn으로..pypy3 으로..
a = int(input())
result = []
for i in range(a):
    result.append(int(input()))
result.sort()
for j in range(a):
    print(result[j])