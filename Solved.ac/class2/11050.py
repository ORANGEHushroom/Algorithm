from math import factorial

n,k = map(int,input().split())

print(factorial(n)//(factorial(k)*factorial(n-k)))


# def a(x):
#      b=1
#      for i in range(1,x+1):
#           b=b*i
#      return b
# b,c=map(int,input().split())
# print(a(b)//a(c)//a(b-c))