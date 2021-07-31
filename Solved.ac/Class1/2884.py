x,y = map(int,input().split())
if x == 0:
    
    if y < 45:
        x = 23
        z = 60+y-45
        print(f'{x} {z}')
    else:
        print(f'{x} {y-45}')
elif x > 0:
    if y < 45:
        z = 60+y-45
        print(f'{x-1} {z}')
    else:
        print(f'{x} {y-45}')
    
         



    

