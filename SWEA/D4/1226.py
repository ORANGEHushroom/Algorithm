import sys
sys.stdin = open('1226.txt')
# 우 하 상 좌
dx = [1,0,0,-1]
dy = [0,1,-1,0]


def bfs(x,y):
    queue = [[x,y]]
    visited = [[0]*16 for _ in range(16)]
    while queue:
        x,y = queue.pop(0)
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if road[nx][ny] == 3:
                return 1
            if road[nx][ny] == 0 and visited[nx][ny] !=1 and 0<=nx<=15 and 0<=ny<=15:
                queue.append([nx,ny])
            
    return 0



for tc in range(1, 11):
    n = int(input())
    print('#{}'.format(tc), end=" ")
    road = [list(map(int,input())) for _ in range(16)]
    # 1 벽 0 길 2 출발 3 도착
    for i in range(16):
        for j in range(16):
            if road[i][j] == 2:
                x, y = i, j
    print(bfs(x,y))

# dfs
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# for _ in range(10):
#     answer = 0
#     n = int(input())
#     maps = [list(input()) for _ in range(16)]

#     # 출발점 찾기
#     x, y = 0, 0
#     for i in range(16):
#         for j in range(16):
#             if maps[i][j] == '2':
#                 x, y = i, j

#     # 미로탐색 DFS
#     stack = [(x, y)]
#     while stack:
#         cx, cy = stack.pop()
#         for k in range(4):
#             nx = cx + dx[k]
#             ny = cy + dy[k]
#             if 0 <= nx < 16 and 0 <= ny < 16:
#                 # 길을 만날 경우
#                 if maps[nx][ny] == '0':
#                     stack.append((nx, ny))
#                     maps[nx][ny] = '9'
#                 # 끝점을 만날 경우 
#                 elif maps[nx][ny] == '3':
#                     answer = 1
#                     stack.clear()
#                     break

#     print('#{} {}'.format(n, answer))