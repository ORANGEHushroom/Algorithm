T = int(input())
for TC in range(1, T+1):
    arr = list()
    N, M = map(int,input().split()) #총 크기, 찾을 글자

    for i in range (N):#가로
        string = str(input()) 
        arr.append(string) #모형 만들고
        for j in range(0,N-M+1): #상자크기 n보다m이 작으니까 여유분만큼.. 
            # 몇번 구할수잇을지 
            end = M+j #끝은 글자수 에 j여유분 더한거
            if string[j:end] == string[j:end][::-1]: #한줄의 글자수만큼 반전해도같으면
                ans = string[j:end] #정답!
    #세로
    vertArr = list() #빈리스트 만들어놓고

    for j in range(0,N):
        vertStr = str()
        vert = list()
        for i in range(0,N):
            vert.append(arr[i][j])#세로줄마다 한 좌표씩 넣기
        vertStr = ''.join(vert) #조인으로 합체
        vertArr.append(vertStr)#줄마다 덩어리
        for k in range(0,N-M+2): #위랑동일
            end = M+k
            if vertStr[k:end] == vertStr[k:end][::-1] : #회문이면
                ans = vertStr[k:end]
    
    print('#{} {}'. format(TC,ans))