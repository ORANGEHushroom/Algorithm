N = int(input())
a = []
for i in range(1, N+1):
    if N % i == 0:
        a.append(i)
a.sort()
for j in a:
    print(j, end=" ")
