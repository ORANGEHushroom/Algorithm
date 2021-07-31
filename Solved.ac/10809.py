a = 'abcdefghijklmnopqrstuvwxyz'
b = input()
for i in range(len(a)):
    if a[i] in b:
        print(b.index(a[i]), end=" ")
    else:
        print(-1, end= " ")   




# sol2)
# import string

# a = string.ascii_lowercase
# b = input()
# for i in range(len(a)):
#     if a[i] in b:
#         print(b.index(a[i]), end=" ")
#     else:
#         print(-1, end= " ")    


# sol3)
# import string
# a = input()
# for i in string.ascii_lowercase:
#     print(a.find(i),end=" ") #find는 알아서 -1반환


# sol4)
# word = input()
# alphabet = list(range(97,123))  # 아스키코드 숫자 범위

# for x in alphabet :
#     print(word.find(chr(x))) 