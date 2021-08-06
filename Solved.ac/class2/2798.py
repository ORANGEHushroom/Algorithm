a,b = map(int,input().split())
arr = list(map(int,input().split()))
result = 0
for i in range(a):
    for j in range(i+1,a):
        for k in range(j+1,a):
            if arr[i]+arr[j]+arr[k] > b:
                continue
            else:
                result = max(result,arr[i]+arr[j]+arr[k])
print(result)


# combibations임폴트해서 활용가능!
# from itertools import combinations
# N, M = map(int, input().split()) 
# nums = list(map(int, input().split())) 
# result = 0 
# for cards in combinations(nums, 3): 
#     sum_num = sum(cards) 
#     if sum_num <= M and sum_num > result: 
#         result = sum_num 
# print(result)

