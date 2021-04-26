# 보너스(for)
# 아래와 같은 모양으로 출력하는 프로그램을 작성하시오.
# 사용자에게 숫자를 입력받아 입력 받은 높이 만큼의 삼각형을 출력하시오.
# 입력 예: 5

height = int(input("높이를 입력하시오."))
sum = ""
for i in range (1,height+1):
    sum = sum + "*"
    print(sum)
