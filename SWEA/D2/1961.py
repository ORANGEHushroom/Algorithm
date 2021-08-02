T = int(input())

for t in range(1, T+1) :
    N = int(input())

    input_matrix = [[''] * N for i in range(N)]
    for i in range(N) :
        row = input().split()
        for j in range(N) :
            input_matrix[i][j] = row[j]

    output_matrix = [[''] * 3 for i in range(N)]

    # 90도 회전
    for i in range(N) :
        for j in range(N) :
            output_matrix[i][0] += input_matrix[N-1-j][i]
    # 180도 회전
    for i in range(N) :
        for j in range(N) :
            output_matrix[i][1] += input_matrix[N-1-i][N-1-j]
    # 270도 회전
    for i in range(N) :
        for j in range(N) :
            output_matrix[i][2] += input_matrix[j][N-1-i]

    print("#{}".format(t))
    for i in range(N) :
        print(*output_matrix[i])