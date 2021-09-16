import sys
sys.stdin = open('12051.txt')

t = int(input())
for tc in range(1,t+1):
    total, pd, pg = map(int,input().split()) #1 12 123 111111  
    # 
    # 확률이니까 
    # 1자리고 10이상이면 무조건 1 2   0.1 0.2   10 
    # 2자리고 100보다 크면 무조건 12 23  0.12 0.23  100   12 23
    # 3자리이고 1000보다 크면 무조간
    # 곱햇을떄1 나오면 무조건 
    # pg pd가 0 100 으로만 이루어져잇다면 무조건
    a = total // 10
    b = pd // 10
    c = pg //10
    if [pd, pg] == [0,0] or [pd, pg] == [100,100]: 
        print('#{} {}'.format(tc, 'Possible'))
        continue
    elif [pd, pg] == [100,0] or [pd, pg] == [0,100]:
        print('#{} {}'.format(tc, 'Broken'))
        continue
    else:
        if a > b and a > c:
            print('#{} {}'.format(tc, 'Possible'))
            continue
        #if (total//10) >= 1 and (pd //10) <= 0 and (pg // 10) <= 0:
        #if total//10 >= 2 and pd //10 <= 1 and pg //10 <=1 :
        
        # pd pg의 배수여야하고 그 d g 값이 토탈을 안넘어야함

        pd2, pg2 = pd/(10**b), pg/(10**c) # 12 0.12
        num = 0
        for d in range(1,total+1):
            if pd2 * d == 1:
                num += 1
        for g in range(1,total+1):
            if pg2 * g == 1:
                num += 1
        if num == 2: # 0.81 0.83 이면
            print('#{} {}'.format(tc, 'Possible'))
        else:     
            print('#{} {}'.format(tc, 'Broken'))






            