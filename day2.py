이름 = input("이름을 입력하세요: ")
print("안녕하세요,", 이름)
#input("메시지") → 메시지를 보여주고 입력을 기다림
#입력된 값은 문자열(str) 로 저장돼
#숫자로 쓰고 싶으면 int()나 float()로 감싸면 돼

나이 = int(input("나이를 입력하세요: "))
print("내년엔", 나이 + 1, "살이 되겠네요!")

색 = input("좋아하는 색은? ")
print("나도", 색, "좋아해!")


a = int(input("첫 번째 숫자: "))
b = int(input("두 번째 숫자: "))
print("두 수의 합은", a + b)


온도 = float(input("오늘 온도는 몇 도야? "))
print("오~", 온도, "도면 좀 덥겠네")


x, y = input("두 개의 숫자를 띄어쓰기로 입력: ").split()
print("합:", int(x) + int(y))


while True:
    말 = input("하고 싶은 말(끝내려면 quit 입력): ")
    if 말 == "quit":
        break
    print("너가 한 말:", 말)
# while True: → 무한 반복 시작
# input()으로 말 입력받음
# 만약 입력이 "quit"이면 break로 반복 종료
# 아니면 입력한 말 그대로 출력

# 파일 수정 → Add → Commit → Push 이 순서 꼭 지켜야 안전
# Git: Status로 현재 상태 확인 가능