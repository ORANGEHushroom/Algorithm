import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc), end=" ")
    n, m = map(int, input().split())
    li = [list(map(str, input())) for _ in range(n)]

    for i in range(len(li)):
        if '1' in li[i]:
            num = li[i]
            break
    # 0000011101101100010111011011000101100010001101001001101110110000000000
    for j in range(len(num)-1, -1, -1): #10 -> 0~9 -> 9~-1
        if num[j] == '1': # 5
            a = j
            break # 맨 뒤의 1
    # print(a) # 59 니까 56
    fin = [] #
    for k in range(a-55, a+1, 7):
        # 53~59 -> 53~60 -> 53 46 39 32 25 18 11 4
        fin.append(num[k:k+7]) # 3~9
    #print(fin)
    last = []
    for c in range(len(fin)):
        last.append(''.join(map(str, fin[c])))
    # print(last)
    # ['0011101', '1011000', '1011101', '1011000', '1011000', '1000110', '1001001', '1011101', '1000000']
    #print(len(last))
    number = []
    for z in range(len(last)):
        if last[z] == '0001101':
            number.append('0')
        elif last[z] == '0011001':
            number.append('1')
        elif last[z] == '0010011':
            number.append('2')
        elif last[z] == '0111101':
            number.append('3')
        elif last[z] == '0100011':
            number.append('4')
        elif last[z] == '0110001':
            number.append('5')
        elif last[z] == '0101111':
            number.append('6')
        elif last[z] == '0111011':
            number.append('7')
        elif last[z] == '0110111':
            number.append('8')
        elif last[z] == '0001011':
            number.append('9')
    # print(number) #['7', '5', '7', '5', '5', '0', '2', '7']
    total = 0
    for i in range(1, 9): # 0~7 1~8
        if i % 2: # 홀수라면 number
            total += int(number[i-1])*3
        else:
            total += int(number[i-1])
    fin_fin = 0
    if total % 10 == 0:
        for v in number:
            fin_fin += int(v)
        print(fin_fin)
    else:
        print('0')
