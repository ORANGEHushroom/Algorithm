N = int(input())

for i in range(N):
    a = input()
    score = 0
    sumScore = 0
    for j in a:
        if j == 'O':
            score += 1
        else:
            score = 0
        sumScore += score #안에안넣고 밖에꺼내도 되는듯!
    print(sumScore)
