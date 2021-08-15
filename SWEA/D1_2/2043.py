a, b = map(int,input().split())
count = 0
for i in range(b, a+1):
    count += 1
print(count)


p, k = map(int,input().split()) 
n = 1
while p > k :
    k += 1
    n += 1
print(n)

a, b = map(int,input().split())
print(abs(a)-abs(b)+1)