import sys
from collections import Counter

T = int(input())
a = []
for _ in range(1, T+1):
    a.append(int(input()))
a.sort()
print(round(sum(a)/T))
print(a[T//2])

counter_a = Counter(a).most_common()
if len(counter_a) > 1:
    if counter_a[0][1] ==counter_a[1][1]:
        print(counter_a[1][0])
    else:
        print(counter_a[0][0])
else:
    print(counter_a[0][0])


print(a[-1]-a[0])

# 밑은 시간초과나는식

import sys

n = int(sys.stdin.readline())

li = []
for i in range(1, n+1):
    li.append(int(sys.stdin.readline()))
print(round(sum(li)/n))

print(li[n//2])
cnt = {} 
newli = list(map(str,li))
for i in newli:
    cnt[i] = newli.count(i)
a = max(cnt.values())
ans = []
for x,y in cnt.items():
    if y == a:
        ans.append(int(x))

if len(ans) > 1:
    ans.sort()
    print(ans[1])
else:
    print(*ans)
print(max(li)-min(li))