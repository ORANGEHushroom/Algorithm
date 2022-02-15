# set 쓰는게 직효네.. 이분탐색안쓰려고 별짓다하다가..
import sys

n = sys.stdin.readline()#int(sys.stdin.readline())
ln = set(sys.stdin.readline().split())
m = sys.stdin.readline()#int(sys.stdin.readline())
lm = list(sys.stdin.readline().split())
for i in lm:
    if i in ln:
        print(1)
    else:
        print(0)
