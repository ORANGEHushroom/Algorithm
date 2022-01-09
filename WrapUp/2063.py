n = int(int(input())/2)
num = list(map(int, input().split()))
num.sort()
print(num[n])

# a = sorted(map(int,input().split()))  그냥 이렇게 해도되는게
# sorted 자체가 리스트를 반환하기떄문이래..