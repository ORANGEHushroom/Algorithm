a = list(map(int,input().split()))
b = 0
for i in a:
    b += i**2
total = b % 10
print(total)     