import sys
from collections import Counter

T = int(input())
a = []
for _ in range(1, T+1):
    a.append(int(input()))
a.sort()
print(round(sum(a)/T))
print(a[T//2])

# b = {}
# for i in a:
#     b[i] = a.count(i)
# c = []
# for key, value in b.items():
#     if value == min(b.values()):
#         c.append(key)
# print(c)
# b = []
# for i in a:
#     b.append(a.count(i))
# c = min(b)

# for j in a:
#     if a.count(j) == c and b.count(c) == 1:
#         print(j)
#     elif a.count(j) == c and b.count(c) != 1:
    
# Counter를 사용하여 개수를 세고 most_common()를 통해 빈도수가 높은 순으로 리스트 안을 튜플형태로 반환

counter_a = Counter(a).most_common()
if len(counter_a) > 1:
    if counter_a[0][1] ==counter_a[1][1]:
        print(counter_a[1][0])
    else:
        print(counter_a[0][0])
else:
    print(counter_a[0][0])


print(a[-1]-a[0])
