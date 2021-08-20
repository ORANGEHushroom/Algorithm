T = int(input())
for tc in range(1, T+1):
    a = list(input() for _ in range(5)) #['ABCDE', 'abcde', '01234', 'FGHIJ', 'fghij']
    b = []
    for k in a:
        b.append(len(k))
    max_len = max(b)
    total = [[0]*max_len for _ in range(5)]
    for i in range(5):
        for j in range(max_len):
            if j < len(a[i]):
                total[i][j]=a[i][j] #[['A', 'B', 'C', 'D', 'E'], ['a', 'b', 'c', 'd', 'e'], ['0', '1', '2', '3', '4'], ['F', 'G', 'H', 'I', 'J'], ['f', 'g', 'h', 'i', 'j']]
    new_total = list(map(list,zip(*total)))
    a = ""
    for word in new_total:
        for word2 in word:
            a += word2
    print(a)
    
