a = int(input())
result = []
for i in range(a):
    result.append(int(input()))
result.sort()
for j in range(a):
    print(result[j])

##python3으로는 시간초과가 난다.. 이걸 import sys로 바꾸는 방법도
#생ㄱ가해보자