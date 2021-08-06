sugar=int(input())
bag=0

while sugar>=0:
    if sugar%5==0:
        bag+=(sugar//5)
        print(bag)
        break
    sugar-=3
    bag+=1
else:
    print(-1)

# sugar = int(input()) 
# result = 0 
# while sugar != 0: 
#     if sugar < 0: 
#         result = -1 
#         break 
#     if (sugar % 5) == 0: 
#         result += (sugar // 5) 
#         sugar = 0 
#     else: 
#         sugar -= 3 
#         result += 1 
# print(result)
