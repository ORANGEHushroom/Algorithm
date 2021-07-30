T = int(input()) # testcase 개수

for tc in range(T): #3 tc = 0,1,2
    # 이 아래부터 실질적인 코드 작성
    numbers = input()
    # '3 17 1 39 8 41 2 32 99 2' 형식이라 리스트로 바꾸자
    numbers = numbers.split() #띄어쓰기를 중심으로 나눈다는뜻 ['3','17',,,] 됨
    
    numbers = list(map(int, numbers)) #다른 자료구조를 정수로 바꿈 #[3, 17, 1, 39,,]
    total = 0
    for number in numbers:
        if number % 2 == 1:
            total += number

    print(f'#{tc+1} {total}')
    # => #1 203
