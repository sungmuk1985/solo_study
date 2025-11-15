age = int(input("나이 입력: "))

if age >= 20:
    print("성인이야")
else:
    print("미성년자야")


score = int(input("점수 입력: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")


temp = int(input("현재 온도: "))

if temp >= 25 and temp <= 30:
    print("딱 좋은 날씨")
else:
    print("온도 조절 필요")


food = input("좋아하는 음식: ")

if food == "치킨":
    print("너 치킨 좋아하네?")
elif food == "피자":
    print("피자 좋아하는구나")
else:
    print("그것도 맛있지")


pw = input("비밀번호 입력: ")

if pw == "1234":
    print("로그인 성공")
else:
    print("비밀번호 틀림")
