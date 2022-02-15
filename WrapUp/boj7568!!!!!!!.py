#예전에 푼 방법
num_student = int(input())
student_list = []

for _ in range(num_student):
    weight, height = map(int, input().split())
    student_list.append((weight, height))

for i in student_list:
    rank = 1
    for j in student_list:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")


#쓸데없이 복잡하게풀엇으며 심지어 틀림 ㅎ

# n = int(input())
# #4 2 6
# #3 3 6
# #1 1 2
# #2 4 6
# #5 5 10
# li1 = [0]
# li2 = [0]
# for tc in range(1, n+1):
#     w, h = map(int,input().split())
#     li1.append(w)
#     li2.append(h)
# newli1 = sorted(li1)
# newli2 = sorted(li2)

# num = []
# a = 0
# for i in range(1,n+1):
#     for j in range(1, n+1):
#         if li1[i] == newli1[j]:
#             a += j
#         if li2[i] == newli2[j]:
#             a += j
#     num.append(a)
#     a = 0
# #print(num) #[6, 6, 10, 6, 2]
# rank = sorted(num, reverse=True) #[10,6,6,6,2]
# for k in num:
#     for i in range(1,len(rank)+1):
#         if k == rank[i-1]:
#             print(i, end=" ")
#             break



