a = []
for i in range(10):
    n = int(input())
    a.append(n)
b = []
for i in a:
    b.append(i % 42)
total = len(set(b))
print(total)      


#sol2)
# arr = []
# for i in range(10):
#     n = int(input())
#     arr.append(n % 42)
# arr = set(arr)
# print(len(arr))