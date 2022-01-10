import sys
sys.stdin = open('input.txt')

t = int(input()) 
for tc in range(1, t+1):
    
    n = int(input())
    total = 0
    print(f'#{tc}')
    for i in range(n):
        a, b = input().split() #int아니면 map안써도됨 주의
        
        for j in range(int(b)):
            print(a,end="")
            total+=1
            if total % 10 == 0 and total > 0:
                #print("\n") 이거 아니고
                print() #이거!
    print()
