a = [1,2,3,4,5,6,7,8]

b = list(map(int,input().split()))

if b == a:
    print('ascending')
elif b == a[::-1]:
    print('descending')

else:
    print('mixed')
    

# 백준풀이1) a=input()[2::2];print({a:"mixed","2345678":"ascending","7654321":"descending"}[a])
#sol2) d=input().split();s=sorted(d);print((('mixed','descending')[s[::-1]==d],'ascending')[s==d])