n = int(input())
li = []
for i in range(1, n+1):
    age, name = input().split()
    li.append([int(age), name, i])
li.sort(key= lambda x: x[2])
li.sort(key= lambda x : x[0])
for i in li:
    print(f'{i[0]} {i[1]}')