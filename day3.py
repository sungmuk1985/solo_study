# 1. 산술 연산자 문제
# 문제: a 와 b 를 이용해 각각의 결과를 출력해봐.
a = 15
b = 4

print("더하기:", a + b)
print("빼기:", a - b)
print("곱하기:", a * b)
print("나누기:", a / b)
print("몫:", a // b)
print("나머지:", a % b)
print("제곱:", a ** b)


# 2. 비교 연산자 문제
# 문제: x 가 10보다 큰지, y 와 다른지 출력해봐.
x = 12
y = 12

print("x > 10 ?", x > 10)
print("x != y ?", x != y)


# 3. 논리 연산자 문제
# 문제: num 이 5보다 크고 20보다 작은지 확인.
num = 11

print("5 < num < 20 ?", num > 5 and num < 20)


# 4. 대입 연산자 문제
# 문제: score 에 10을 더한 뒤, 2를 곱해봐.
score = 50
score += 10
score *= 2

print("최종 score:", score)


# 5. 멤버십 연산자 문제
# 문제: "cat" 이 animals 리스트 안에 있는지 확인.
animals = ["dog", "cat", "bird"]

print("cat in animals ?", "cat" in animals)
print("tiger in animals ?", "tiger" in animals)


# 비교·논리 연산자 연습용 코드
# 직접 숫자를 바꿔보면서 결과가 어떻게 달라지는지 확인해봐

# 1. 비교 연산자 테스트
x = int(input("x 값 입력: "))

print("x == 10 :", x == 10)
print("x != 10 :", x != 10)
print("x > 5 :", x > 5)
print("x < 20 :", x < 20)
print("x >= 10 :", x >= 10)
print("x <= 15 :", x <= 15)


# 2. 논리 연산자 테스트
a = int(input("a 값 입력: "))
b = int(input("b 값 입력: "))

print("a > 5 and b < 20 :", a > 5 and b < 20)
print("a < 3 or b > 10 :", a < 3 or b > 10)
print("not (a == b) :", not (a == b))


# 3. 직접 조건 만들어보기
age = int(input("나이 입력: "))

# teenager 조건: 13에서 19 사이
is_teen = age >= 13 and age <= 19

print("teenager 맞나 :", is_teen)


# 4. 조합 연습
num1 = int(input("num1: "))
num2 = int(input("num2: "))
num3 = int(input("num3: "))

avg = (num1 + num2 + num3) / 3

print("평균:", avg)
print("평균이 50 이상이면서 90 미만인가:", avg >= 50 and avg < 90)
print("평균이 100 초과 또는 0 미만인가:", avg > 100 or avg < 0)