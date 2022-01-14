#답은 맞는데 시간초과가 나
##pypy로는 맞음 python3이..
n = int(input())
#1 7 19 37 61
# 1까지 1, 7까지 2... 19- 3 37- 4 61- 5
if n == 1:
    print(1)
else:
    cnt = 2
    w = 0
    ww = 0
    al = 0
    while True:
        if cnt == n:
            break
        cnt += 1
        al += 1
        if al % 6 == 0:
            w += 1
            if w > ww:
                ww = w
                w = 0
                al = 0
    print(ww+2)

## 다른사람 풀이 참고
# import sys

# N = int(sys.stdin.readline())

# honeycomb = 1  
# cnt = 1

# while N > honeycomb:
#     honeycomb += 6 * cnt  
#     cnt += 1  

# print(cnt)

# N = int(input())

# room_count = 2
# plus = 6
# start = 2
# end = start + plus - 1

# if N != 1:
#     while True:
#         if N >= start and N <= end:
#             break
#         else:
#             start = end + 1
#             plus += 6
#             end = start + plus - 1
#             room_count += 1
# else:
#     room_count = 1
    
# print(room_count)