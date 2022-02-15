t = int(input())
for tc in range(1, t+1):
    words = input()
    stack = []
    flag = True
    for i in words:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                print("NO")
                flag = False
                break
            else:
                stack.pop()
    if stack:
        flag = False
        print("NO")
    elif flag == True and not stack:
        print("YES")