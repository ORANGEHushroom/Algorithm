T = int(input())
for tc in range(1,T+1):
    num = int(input())
    a = list(map(int,input().split()))
    a.sort()
    print(f'#{tc}', *a)  # * 은 A = [1,2,3] 을 1 2 3 으로 해제시켜줌
#  total=a.sort()
#    print(f'#{tc}', *total)   에러나는 이유는 SORT의 문제... total = sorted(a)하면됨
    


# T = int(input())
# for test_case in range(1,T+1):
#     N = int(input())
#     list_num = list(map(int,input().split()))
#     list_num.sort()
 
#     print(f'#{test_case} ',end='')
#     print(*list_num)

