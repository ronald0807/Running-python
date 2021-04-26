
# 문제 9.
# 1~12사이의 정수를 입력받아 평년의 경우 입력받은 월을 입력받아 평년의 경우 해당 월의 날수를 출력하는 프로그램을 작성하시오.
# 평년의 경우 1월부터 12월까지 일수는 각각 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31일이다.
# 입력 예: 2
# 출력 예: 28

month = int(input("월을 입력하시오."))

if month == 1 or month ==3 or month ==5 or month ==7 or month ==8 or month ==10 or month ==12:
    print(31)
elif month == 4 or month ==6 or month ==9 or month ==11 :
    print(30)
else :
    print(28)
