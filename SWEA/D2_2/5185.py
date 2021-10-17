import sys
sys.stdin = open('5185.txt')

t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc),end=" ")
    n, word = map(str,input().split())
    n = int(n)
    new_word = []
    for i in range(n):
        if word[i] == 'A':
            new_word.append(10)
        elif word[i] == 'B':
            new_word.append(11)
        elif word[i] == 'C':
            new_word.append(12)
        elif word[i] == 'D':
            new_word.append(13)
        elif word[i] == 'E':
            new_word.append(14)
        elif word[i] == 'F':
            new_word.append(15)
        else:
            new_word.append(int(word[i]))
    
    total = []
    for i in new_word:
        a = []
        if i > 1:
            while i > 1:
                a.append(i % 2)
                i = i // 2
                if i == 1:
                    a.append(i)
                    break
        else:
            a.append(i)
        if len(a) == 4:
            total.append(a[::-1])
        else:
            for j in range(4-len(a)):
                a.append(0)
            total.append(a[::-1])
    
    fin_fin = ""
    for i in range(len(total)):
        for j in range(4):
            fin_fin += str(total[i][j])
    print(fin_fin)
