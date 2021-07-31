a = 'abcdefghijklmnopqrstuvwxyz'
b = input()
for i in range(len(a)):
    if a[i] in b:
        print(b.index(a[i]), end=" ")
    else:
        print(-1, end= " ")   