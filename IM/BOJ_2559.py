# total, num = map(int,input().split())
# day = list(map(int,input().split()))

# result = []
# for i in range(total):
#     a = day[i:i+num]
#     if len(a) == num:
#         result.append(sum(a))
# print(max(result))

# total, num = map(int,input().split())
# day = list(map(int,input().split()))
# i = 1
# result = []
# while i + num - 1 <= total: #1+5+5-1=10
#     result.append(sum(day[i-1:i+num-1])) #day[0:5]
#     i += 1
# print(max(result))

# 건영님
N, K = map(int, input().split())    # n = 100,000 -> O(n^2) 시간초과 주의
arr = list(map(int, input().split()))

result = 0
for i in range(K):
    result += arr[i]

max_num = result
for i in range(K, N):
    result += (arr[i] - arr[i-K])   # 점화식 부분
    if max_num < result:
        max_num = result

print(max_num)