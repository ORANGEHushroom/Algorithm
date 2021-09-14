import sys
sys.stdin = open('1946.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    li = []
    for n in range(N):
        alpha, num = map(str,input().split()) 
        for _ in range(int(num)):
            li.append(alpha)
    print('#{}'.format(tc))
    for i in range(1,len(li)): #22
        if i % 10 == 1 and i + 9 < len(li): # 1~10 11~ 20 21~22
            a = li[i-1:i+9]
            for k in a:
                print(k, end="")
            print()
        elif i % 10 == 1 and i + 9 > len(li):
            b = li[i-1:]
            for j in b:
                print(j, end="")
            print()
            

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     lst = ''
#     for i in range(N):
#         alphabet, num = input().split()
#         num = int(num)
#         for i in range(num):
#             lst += alphabet
#     print('#{}'.format(tc))
#     for j in range(0, len(lst), 10):
#         print(lst[j:j+10])

# T = int(input())
# for tc in range(1,T+1):
#     Answer =''
#     j = 0
#     N = int(input())
#     for _ in range(N):
#         C, K = map(str, input().split())
#         Answer += C*int(K)
#     print('#{}'.format(tc))
#     for i in Answer:
#         print(i, end="")
#         j += 1
#         if j % 10 == 0:
#             print()
#     print()