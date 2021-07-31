total = []
for numbers in range(9): #9번 반복하기 위해 range(9)를 범위로 설정하여 for문을 작성한다. 
    #1회 반복할 때마다 num_list에 int(input())으로 입력값을 append한다.
    total.append(int(input()))

x = max(total)
print(x)
print(total.index(x)+1)
    