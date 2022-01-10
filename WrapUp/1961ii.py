import sys
sys.stdin = open('input.txt')
#풀다말앗는데 싸피방법이 더 조은듯..는 다른분꺼 긁어옴^^
#sol1)
def rotate(N, matrix):
    result = []
    for i in range(3):
        matrix90 = [[0 for _ in range(N)] for _ in range(N)]

        for i in range(N):
            for j in range(N):
                matrix90[j][N-1-i] = matrix[i][j]
        result.append(matrix90)
        matrix = matrix90
    return result

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    result = rotate(N, matrix)
    print('#{}'.format(tc))
    for i in range(N):
        for item in result:
            print(*item[i],sep='',end=' ')
        print()

#sol2)

T = int(input())

def rotate_puzzle(list1, n):
    puzzle = []
    for i in range(n):
        temp = []
        for e in list1[::-1]:
            temp.append(str(e[i]))
        puzzle.append(temp)
    return puzzle


for tc in range(T):
    N = int(input())
    puzzle_0 = [list(map(int, input().split())) for _ in range(N)]
    puzzle_90 = rotate_puzzle(puzzle_0, N)
    puzzle_180 = rotate_puzzle(puzzle_90, N)
    puzzle_270 = rotate_puzzle(puzzle_180, N)

    print(f'#{tc + 1}')
    for n in range(N):
        print(''.join(puzzle_90[n]), ''.join(puzzle_180[n]), ''.join(puzzle_270[n]))