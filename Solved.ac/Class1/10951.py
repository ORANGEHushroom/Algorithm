import sys
for line in sys.stdin:
    a, b = map(int, line.split())
    print(a+b)

    
# while True:
#     try:
#         A, B = map(int, input().split())
#         print(A+B)
#     except:
#         break   