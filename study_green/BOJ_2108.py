T = int(input())
a = []
for _ in range(1, T+1):
    a.append(int(input()))
a.sort()
print(round(sum(a)/T))
print(a[T//2])

# b = {}
# for i in a:
#     b[i] = a.count(i)
# c = []
# for key, value in b.items():
#     if value == min(b.values()):
#         c.append(key)
# print(c)
b = []
for i in a:
    b.append(a.count(i))
c = min(b)

for j in a:
    if a.count(j) == c and b.count(c) == 1:
        print(j)
    elif a.count(j) == c and b.count(c) != 1:
        
    
print(a[-1]-a[0])
