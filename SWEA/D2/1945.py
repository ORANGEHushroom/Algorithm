for T in range(1, int(input()) + 1):
    n = int(input())
    div_list = [2, 3, 5, 7, 11]
    div_count = [0] * 5
    for i in range(len(div_list)):
        while n % div_list[i] == 0:
            n /= div_list[i]
            div_count[i] += 1

    print(f'#{T} {div_count[0]} {div_count[1]} {div_count[2]} {div_count[3]} {div_count[4]}')