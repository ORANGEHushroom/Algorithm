li = list(map(int,input().split()))
result = [1,1,2,2,2,8]
for i in range(len(li)):
    print(result[i]-li[i],end=" ") 