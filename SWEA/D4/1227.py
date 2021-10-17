import sys
sys.stdin = open('1227.txt')

dx = [1,0,0,-1]
dy = [0,1,-1,0]


def bfs(x,y):
    queue = [[x,y]]
    visited = [[0]*100 for _ in range(100)]
    while queue:
        x,y = queue.pop(0)
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if road[nx][ny] == 3:
                return 1
            if road[nx][ny] == 0 and visited[nx][ny] !=1 and 0<=nx<=99 and 0<=ny<=99:
                queue.append([nx,ny])
            
    return 0


for tc in range(1, 11):
    n = int(input())
    print('#{}'.format(tc), end=" ")
    road = [list(map(int,input())) for _ in range(100)]
    # 1 벽 0 길 2 출발 3 도착
    for i in range(100):
        for j in range(100):
            if road[i][j] == 2:
                x, y = i, j
    print(bfs(x,y))
