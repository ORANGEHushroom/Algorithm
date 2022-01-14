
# 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
#“a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터
#  b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다”
"""

1 5 15 35 70     
1 4 10 20 35 56    -> 2층
1 3 6 10 15 21   -> 1층
1 2 3 4  5  6  7 -> 0층
n이 구해지면 그 바로 밑 층만 구해서 더하자!
코드수정...
런타임에러 방지...
n -> 밑층은 1, n -1 +2, n+2, ...
"""
# 다른사람풀이..인데 쩐다..규칙찾는게 중요
t = int(input())
d = [[0]*15 for i in range(15)]

for i in range(1, 15):
    d[0][i] = i
for i in range(1, 15):
    for j in range(1, 15):
        d[i][j] = d[i][j-1] + d[i-1][j]
# for i in d:
#     print(*i)
for i in range(t):
    k = int(input())
    n = int(input())
    print(d[k][n])