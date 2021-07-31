

a = str(input())
b = [0]*len(a)
c = 0
for i in a:
    b[c]=a.count(i)
    c+=1
max_num = b[0]
for j in b:
    if j > max()