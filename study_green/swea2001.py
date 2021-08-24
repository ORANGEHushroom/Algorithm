import sys
sys.stdin = open('input_fly.txt')

T = int(input())
for tc in range(1, T+1):
    box, weapon = map(int, input().split())
    result = [list(map(int,input().split())) for _ in range(box)]
    fin_fin = []
    for i in range(box):
        for j in range(box):
            total = []
            for k in range(i,i+weapon):  
                for p in range(j,j+weapon):
                    if k >= box or p >= box:
                        continue
                    total.append(result[k][p])
            final_fly = sum(total)
            fin_fin.append(final_fly)
    max_fly = fin_fin[0]
    for ele in fin_fin:
        if ele > max_fly:
            max_fly = ele
    print('#{} {}'.format(tc, max_fly))
