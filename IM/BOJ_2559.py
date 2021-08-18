total, num = map(int,input().split())
day = list(map(int,input().split()))
i = 1
result = []
while i + num - 1 <= total: #1+5+5-1=10
    result.append(sum(day[i-1:i+num-1])) #day[0:5]
    i += 1

print(max(result))

#시간초과나서 마상...8ㅅ8