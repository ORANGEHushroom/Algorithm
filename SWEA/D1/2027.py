for i in range(1,6):
    for j in range(1,6):
        if i == j:
            print('#',end='')
        else:
            print('+',end='')
    print() # 포문한번 돌때마다 프린트해주기위해 