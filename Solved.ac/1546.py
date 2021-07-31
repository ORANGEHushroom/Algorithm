a = int(input())
b = list(map(int,input().split()))
max_num = max(b)
for i in range(a):
    b[i] = b[i]/max_num*100
print(sum(b)/a)