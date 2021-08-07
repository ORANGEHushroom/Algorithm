x,y = map(int,input().split())
a = []
b = []
for i in range(1, x+1):
    if x % i == 0:
        a.append(i)
for j in range(1, y+1):
    if y % j == 0:
        b.append(j)
c = []
for k in a:
    if k in b:
        c.append(k)
print(max(c))

print((x*y)//(max(c)))

# num = 2
# total = 1
# while True:
#     if num < min(x,y):
#         if x % num ==0 and y % num == 0:
#             total * num
#         elif x % num !=0 or y % num != 0:
#             num += 1
#     else:    
#         print(total)