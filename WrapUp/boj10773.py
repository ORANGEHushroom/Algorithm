t = int(input())
li = []
for _ in range(1, t+1):
    n = int(input())
    if n == 0:
        li.pop()
    else:
        li.append(n)
    
print(sum(li))