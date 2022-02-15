from collections import deque
n, k = map(int, input().split())
s = deque([])
for i in range(1, n + 1):
    s.append(i)
print('<', end='')
while s:
    for i in range(k - 1):
        s.append(s[0])
        s.popleft()
    print(s.popleft(), end='')
    if s:
        print(', ', end='')
print('>')

#이렇게 출력도 조은듯..
# print("<", ", ".join(r), ">", sep="")

#일단 밑은 틀림
# n, k = map(int,input().split())
# stack = []
# for i in range(1, n+1):
#     stack.append(i)
# li = []
# k = 3
# # 1 2 3 4 5 6 7   
# while stack:
#     if len(stack) >= k and len(stack) > 2:
#         a = stack.pop(k-1)
#         li.append(str(a))
#         k -= 1
#         k += 3
#     elif len(stack) <= 2:
#         a = stack.pop(0)
#         li.append(str(a))
#     else:
#         k = k - len(stack)
#         a = stack.pop(k-1)
#         li.append(str(a))
#         k -= 1
#         k += 3
# # for i in li:
# #     print(','.join(i), end=", ")
# print("<", end='')
# print(', '.join(li),end='')
# print(">")
