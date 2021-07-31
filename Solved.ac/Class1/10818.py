a = int(input())
b = list(map(int,input().split()))
max_num = b[0]
min_num = b[0]
for i in range(a):
    if b[i] > max_num:
        max_num = b[i]
for i in range(a):
    if b[i] < min_num:
        min_num = b[i]    

print(f'{min_num} {max_num}') 