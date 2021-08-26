## 미완

# for tc in range(4):
#     x11,y11, x12, y12, x21, y21, x22, y22 = map(int, input().split())
#     box = [[0]*50000 for _ in range(50000)]
#     for i in range(x11, x12+1):
#         for j in range(y11, y12+1):
#             box[i][j] += 1
#     for k in range(x21, x22+1):
#         for z in range(y21, y22+1):
#             box[k][z] += 1
#     if box.count(2) > 0:
#         print('a')
#     elif box.count(2) == 0:
#         if x21 == x12 and y21 == y12:
#             print('c')
#         elif x21 == x11 and y21 == y11:
#             print('c')
#         elif x22 == x12 and y22 == y12:
#             print('c')
#         elif x22 == x11 and y22 == y11:
#             print('c')



for i in range(4):

    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split()) 
    xl = max(x1, x2) # 아래쪽 X들의 최대
    xr = min(p1, p2) # 위쪽 X들의 최소 
    yb = max(y1, y2) # Y들의 최대
    yt = min(q1, q2) # Y들의 최소
    xdiff = xr - xl 
    ydiff = yt - yb  
    if xdiff > 0 and ydiff > 0: 
        print('a') 
    elif xdiff < 0 or ydiff < 0: 
        print('d') 
    elif xdiff == 0 and ydiff == 0: 
        print('c') 
    else: 
        print('b')

