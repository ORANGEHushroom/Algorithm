while True:
    li = list(map(int, input().split()))
    li.sort()
    if li == [0,0,0]:
        break
    else:
        if li[-1] ** 2 == li[0] ** 2 + li[1] ** 2:
            print("right")
        else:
            print("wrong")
        
