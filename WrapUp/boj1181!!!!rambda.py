t = int(input())
li = []
for tc in range(1, t+1):
    li.append(input())
newli = list(set(li))

newli.sort()
newli.sort(key= lambda x : len(x))
for i in newli:
    print(i)
#sol3
#람다 안쓸거면 이것도 가능
# T = int(input())
# a = []
# for tc in range(1,T+1):
#     a.append(input())
# b = list(set(a))
# b.sort()    
# result_total = sorted(b,key=len)
# for i in range(len(result_total)):
#     print(result_total[i]) 

##너모중요함
#sol1
# #중복 제거
# data_list = list(set(data_list))

# data_list.sort()
# data_list.sort(key=lambda x : len(x))

# print(data_list)

#sol2
# data_list = ['but','i','wont','hesitate','no','more','no','more','it','cannot','wait','im','yours']

# for index in range(len(data_list)) : 
#     data_len = len(data_list[index])
#     data_list[index] = (data_list[index], data_len)

# data_list.sort(key = lambda x :(x[1], x[0]))
# print(data_list)
