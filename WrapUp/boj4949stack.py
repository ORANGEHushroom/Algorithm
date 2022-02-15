#sol1) 런타임에러
#아랜 예전코드..

import sys
sys.stdin = open('input.txt')

while True:
    words = input()
    if len(words)== 1 and words == '.':
        break
    else:
        word = list(words.split())
        s1 = []
        flag = 1
        try:
            for i in word:
                for j in i:
                    if j == '(':
                        s1.append(j)
                    elif j == '[':
                        s1.append(j)
                    elif j == ')':
                            a = s1.pop()
                            if a != '(':
                                print("no")
                                flag = 0
                                break
                        
                    elif j == ']':
                            a = s1.pop()
                            if a != '[':
                                print("no")
                                flag = 0
                                break
            if flag != 0 and len(s1) == 0:
                print("yes")
        except:
            print("no")
            
        
#sol2)
import sys 
input = sys.stdin.readline


while True:
    string = input().rstrip()
    if string == '.':
        break
    stack = []
    temp = True
    for i in string:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[':
                temp = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] == '(':
                temp = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if temp == True and not stack:
        print('yes')
    else:
        print('no')
