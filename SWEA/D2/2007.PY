T = int(input())
 
for tc in range(1, T + 1): 
    string = input()
    pattern =''
    for i in range(1, len(string)+1):
        if string[:i] == string[i:2*i]:
            pattern = string[:i]
            break #답 나와서 이후 포문돌릴필요없으니 스탑

    print(f'#{tc} {len(pattern)}')