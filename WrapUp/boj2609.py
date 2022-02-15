a , b = map(int,input().split())
#최대공약수, 최소공배수
minn = min(a,b)
m = 1#최대공약수

# 1부터 하면 무한루프걸림~
for i in range(2, minn+1):
    while True:
        if a % i == 0 and b % i == 0:
            m *= i
            a = a//i
            b = b//i
        else:
            break
print(m)
print(m*a*b)
#예전 풀이
# x,y = map(int,input().split())
# a = []
# b = []
# for i in range(1, x+1):
#     if x % i == 0:
#         a.append(i)
# for j in range(1, y+1):
#     if y % j == 0:
#         b.append(j)
# c = []
# for k in a:
#     if k in b:
#         c.append(k)
# print(max(c))

# print((x*y)//(max(c)))