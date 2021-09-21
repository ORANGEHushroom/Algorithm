import sys
sys.stdin = open('input_color.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    box = [[0]*10 for _ in range(10)]
    
    for i in range(N):
        x1, y1, x2, y2, color = map(int, input().split()) 
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                if box[x][y] == 0:
                    box[x][y] = color
                elif box[x][y] != 0 and box[x][y] != color and box[x][y] != 3:
                    cnt += 1
                    box[x][y] == 3
                elif box[x][y] != 0 and box[x][y] != color and box[x][y] == 3:
                    continue
                elif box[x][y] != 0 and box[x][y] == color:
                    continue

    print('#{} {}'.format(tc, cnt))
