n = int(input())
li = list(map(int,input().split()))
#소수의 특징 : 루트로 나눈후 제곱햇을때와 같다 or 약수가 2개
cnt = 0
for i in li:
    if i != 1:
        a = 0
        for j in range(1, i+1):
            if i % j == 0:
                a+=1
        if a == 2:    
            cnt+=1

print(cnt)