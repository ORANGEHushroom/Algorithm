
# from math import factorial

# n,k = map(int,input().split())

# print(factorial(n)//(factorial(k)*factorial(n-k)))

n , k = map(int,input().split())
ntotal = 1
for i in range(1, n+1):
    ntotal *= i

ktotal = 1
for i in range(1, k+1):
    ktotal *= i

nminusktotal = 1
a = n - k
for i in range(1, a+1):
    nminusktotal *= i
print(ntotal //(ktotal * nminusktotal))