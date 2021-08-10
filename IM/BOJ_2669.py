arr = [[0] * 100 for _ in range(100)]
cnt = 0
for i in range(4):
    x_l, y_l, x_r, y_r = map(int, input().split())
    for j in range(x_l, x_r):
        for k in range(y_l, y_r):
            if arr[k][j] == 0:
                arr[k][j] = 1
                cnt += 1
print(cnt)