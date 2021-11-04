n = int(input())
lst = list(map(int, input().split()))

s_li = sorted(lst)
li = []
for i in range(n):
    idx = s_li.index(lst[i])
    li.append(idx)
    s_li[idx] = -1
print(*li)