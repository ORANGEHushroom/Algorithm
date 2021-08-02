T = int(input()) 
for i in range(T): 
    H, W, N = map(int, input().split()) 
    tmp_s = N//H 
    tmp_x = N%H 
    if tmp_x == 0: 
        print((H * 100) + tmp_s)
    else: 
        print((tmp_x * 100) + (tmp_s +1))

