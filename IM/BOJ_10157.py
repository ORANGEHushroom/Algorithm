nx = [-1, 0, 1, 0]   #위 오른쪽 아래 왼쪽
ny = [0, 1, 0, -1]

x_size, y_size = map(int, input().split())
audience = int(input())
box = [[0]*y_size for _ in range(x_size)]
for x in range(x_size-1,-1,-1):
    for y in range(y_size):
        box[x_size-1][0] = 1

