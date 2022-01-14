n = int(input())
total = []
for i in range(1,n+1):
    result = 0
    for j in str(i):
        result += int(j)
    result += i
    if result == n:
        total.append(i)

total.sort()
if len(total) == 0:
    print(0)
else:
    print(total[0])

##  간략 버전
# target = int(input())

# for i in range(target):
#     temp = sum(map(int, str(i)))
#     result = i + temp
#     if result == target:
#         print(i)
#         break
# else:
#     print(0)


