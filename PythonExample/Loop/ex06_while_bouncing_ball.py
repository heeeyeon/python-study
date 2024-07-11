# 고무 공을 100 미터 높이에서 떨어뜨리는데,
# 이 공은 땅에 닿을 때마다 원래 높이의 3/5 만큼 튀어오릅니다. 
# 공이 열 번 튀는 동안 튀어오를 때 마다의 높이를 계산합니다.

# 변수 초기화
height = 100
i = 0       
# while절에서 조건을 줄 때 i의 초기화 값이 0이건 1이건 
# i < 10 또는 i <= 10 으로 10회라는 것을 보여줄 수 있으므로 어느쪽이든 상관 없을 것 같다.

while i < 10:
    i += 1
    height = height/5*3
    print(i, ' ', height)
# 결과값으로 출력된 소숫점 자리수가 예제와는 조금 다르다. 이유가 뭘까

# 반올림 함수를 이용해 소숫점 네 번 째 자리까지 출력한다.
# 변수 초기화
height = 100
i = 0       

while i < 10:
    i += 1
    height = height/5*3
    print(i, ' ', round(height, 4))

# 정답에서는 튀어오를때의 높이 감소 비율도 변수에 담았다. 위의 의문점은 해결되지 않았으나..
# 추측: 연산순서가 영향을 주는 듯 하다 -> 나는 5로 먼저 나눈 뒤 3을 곱했고, 정답에서는 3/5 라는 변수자체를 높이값에 곱하게끔 하였다.
# 추측에 따라 연산 순서를 조금 바꾸었으나 여전히 다르다. 문제에서 주어지는 상수값은 변수에 담도록 하자.
height = 100
bounce = 3 / 5

i = 1

while i <= 10:
    height = height * bounce
    print(i, height)
    i = i + 1


height = 100
bounce = 3 / 5

i = 1

while i <= 10:
    height = height * bounce
    print(i, round(height, 4))
    i = i + 1