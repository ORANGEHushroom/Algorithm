day, night, height = map(int,input().split())
if height == day:
    print(1)
else:
    h = day - night#4
    k = height - day#1
    ans = k % h
    if ans == 0:
        print(k // h +1)
    else:
        print(k // h +2)
    # 밑도 되지만 무조건 시간초과날각이라..
    #cnt = 1
    # while True:
    #     if k > h*cnt: # 3 <= 1*1 1*2 1*3
    #         cnt += 1# 1
    #     else:
    #         break
        
# 다른 방법..
# a, b, v = map(int, input().split())
# ls = 0
# if (v - b) % (a - b) != 0:
#     ls = ((v - b) // (a - b)) + 1
# else:
#     ls = ((v - b) // (a - b))
# print(ls)