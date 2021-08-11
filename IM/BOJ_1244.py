switch = int(input())

list_status = list(map(int,input().split()))

num_students = int(input())

for i in range(num_students):

    student_sex, student_number = map(int,input().split())

    if i == 0 or num_students-1:
        continue

