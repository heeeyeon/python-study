print('정수를 입력받아 입력받은 수 만큼 출력하기')
num = int(input('정수 입력: '))
# 반복 횟수를 지정할 변수 초기화
i = 1
while i <= num:
    print(num)
    i += 1

num = int(input())

# 반복 횟수를 지정할 변수 초기화
# 0으로 선언하는 것이 더욱 바람직하다 -> 일반적인 관례이기도 하며
# , 리스트나 범위의 인덱스가 0으로 시작하는 경우가 더 많기 때문이다.
i = 0
while i < num:
    print('', num)
    i += 1