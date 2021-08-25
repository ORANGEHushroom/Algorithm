import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    N = int(input())
    li = list(map(int, input().split()))
    queue = []
    for i in li:
        queue.append(i)

    while queue:
        a == 1

        num = queue.pop(0)
        if a <= 5:
            if num - a <= 0:
                num = 0
                queue.append(num)
                break
            elif num - a > 0:
                queue.append(num - a)
        elif a > 5:
            a = 1
        a += 1
    print('#{} {}'.format(tc, queue))