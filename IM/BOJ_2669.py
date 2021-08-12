arr = [[0] * 100 for _ in range(100)] # 빈 박스 만들기
count = 0
for i in range(4):
    
    xl, yl, x2, y2 = map(int, input().split())
    for j in range(xl, x2):  #박스의 밑
        for k in range(yl, y2): #박스의 높이
            
            if arr[k][j] == 0:  # 좌표가 비어있을때  
                arr[k][j] = 1 # 1넣어주기
                count += 1   #면적 하나 추가해주기
            else:
                continue   #이미 좌표가 차있다면 패스
print(count)