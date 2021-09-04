col, row = map(int,input().split())
li = list(input() for _ in range(row))
#체크할 배열
lis = []
for i in range(col-7): # 10이라고 하면 col 즉 세로 10이니 8이면 3번 가능 
    # 1~8 2~9 3~10
    for j in range(row-7): #13이면 row 즉 가로 13이니 6번 가능
        for k in range(i,i+8): #1~8
            for g in range(j,j+8):
                if li[k][g] == 'B':
                    num = [[0]*8 for _ in range(8)]
                    if k+1 < i+8 and g+1 < j+1 and li[k+1][g] != 'W':
                        num[k+1-i][g-j] = 1
                    elif k+1 < i+8 and g+1 < j+1 and li[k][g+1] != 'W':
                        num[k-i][g+1-j] = 1
                    elif k+1 < i+8 and g+1 < j+1 and li[k+1][g+1] != 'B':
                        num[k+1-i][g+1-j] = 1
                    else:
                        continue
                    total = 0
                    for n in num:
                        total += sum(n)
                    lis.append(total)
                elif li[k][g] == 'W':
                    num = [[0]*8 for _ in range(8)]
                    if k+1 < i+8 and g+1 < j+1 and li[k+1][g] != 'B':
                        num[k+1-i][g-j] = 1
                    elif k+1 < i+8 and g+1 < j+1 and li[k][g+1] != 'B':
                        num[k-i][g+1-j] = 1
                    elif k+1 < i+8 and g+1 < j+1 and li[k+1][g+1] != 'W':
                        num[k+1-i][g+1-j] = 1
                    else:
                        continue
                    total = 0
                    for n in num:
                        total += sum(n)
                    lis.append(total)

print(min(lis))


