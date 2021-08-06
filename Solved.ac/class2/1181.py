T = int(input())
a = []
for tc in range(1,T+1):
    a.append(input())
b = list(set(a))
b.sort()    
result_total = sorted(b,key=len)
for i in range(len(result_total)):
    print(result_total[i]) 
