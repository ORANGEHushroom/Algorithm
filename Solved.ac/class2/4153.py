while True:
    a = sorted(list(map(int,input().split())))
    x = a[0]
    y = a[1]
    z = a[2]
    if x==y==z==0:
        break
    else:
        if z**2==y**2+x**2 :
            print("right")
        else:
            print("wrong")
