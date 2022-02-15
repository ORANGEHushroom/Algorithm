# 메모리 초과가 나는 문제..
# 미리 박스 만들어서 이렇게 0이 아닌걸 체크하는 방식으로
#는 그래도 런타임에러? 차후 확인..
import sys

input = sys.stdin.readline()
num_list = [0] * 10001
n = int(input())
for _ in range(n):
    num_list[int(input())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)