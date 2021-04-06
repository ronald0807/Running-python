# 문제 1.
# 정수를 입력받아 첫 줄에 입력 받은 숫자를 출력하고 둘째 줄에 음수이면 “minus” 라고 출력하는 프로그램을 작성하시오.
# 입력 예1: -5
# 출력 예1:
# -5
# minus
# 입력 예2: 5

# 출력 예2: 5

# num1 = int(input("정수를 입력하시오."))
# print(num1)

# if num1 < 0 :
#     print("minus")


# 문제 2

# “몸무게+100-키”를 비만수치 공식이라고 하자.
# 키와 몸무게를 자연수로 입력받아 첫 번째 줄에 비만수치를 출력하고, 비만수치가 0보다 크면 다음줄에 비만("Obesity")이라는 메시지를 출력하는 프로그램을 작성하시오.
# 입력 예: 155 60
# 출력 예: 5 Obesity

# 몸무게 = int(input("몸무게를 입력하시오."))
# 키 = int(input("키를 입력하시오."))
# 비만수치공식 = 몸무게+100-키
# if 비만수치공식 > 0 :
#     print(비만수치공식)
#     print("Obesity")
# else :
#     print(비만수치공식)



# 문제 3.
# 나이를 입력받아 20살 이상이면 "adult"라고 출력하고 그렇지 않으면 몇 년후에 성인이 되는지를 "○ years later"라는 메시지를 출력하는 프로그램을 작성하시오.
# 입력 예: 18
# 출력 예: 2 years later

# age = int(input("나이를 입력하시오."))

# if age >= 20 :
#     print("adult")
# else :
#     print(20-age, "years later")


# 문제 4.
# 복싱체급은 몸무게가 50.80kg 이하를 Flyweight 61.23kg 이하를 Lightweight, 72.57kg 이하를 Middleweight, 88.45kg 이하를 Cruiserweight, 88.45kg 초과를 Heavyweight라고 하자.
# 몸무게를 입력받아 체급을 출력하는 프로그램을 작성하시오.
# # 입력 예: 87.3
# 출력 예: Cruiserweight

# 몸무게 = float(input("몸무게를 입력하시오."))
# if 몸무게 <= 50.8 :
#     print("Flyweight")
# elif 몸무게 <= 61.23 :
#     print("Lightweight")
# elif 몸무게 <= 72.57 :
#     print("Middleweight")
# elif 몸무게 <= 88.45 :
#     print("Cruiserweight")
# else :
#     print("Heavyweight")


# 문제 5.
# 두 개의 실수를 입력받아 모두 4.0 이상이면 "A", 모두 3.0 이상이면 "B", 아니면 "C" 라고 출력하는 프로그램을 작성하시오.
# 입력 예1: 4.3 3.5
# 출력 예1: B
# 입력 예2: 4.0 2.9
# 출력 예2: C

# num1 = float(input("실수를 입력하시오:"))
# num2 = float(input("실수를 입력하시오:"))

# if num1 and num2 > 4.0 :
#     print("A")
# elif num1 and num2 > 3.0 :
#     print("B")
# else :
#     print("C")


# 문제 6.
# 영문 대문자를 입력받아
# 'A'이면 “Excellent”,
# 'B'이면 “Good”,
# 'C'이면 “Usually”,
# 'D'이면 “Effort”,
# 'F'이면 “Failure”,
# 그 외 문자이면 “error” 라고 출력하는 프로그램을 작성하시오.
# 입력 예: B
# 출력 예: Good


# alp = input("영문 대문자를 입력하시오.")

# if alp == "A" :
#     print("Excellent")
# elif alp == "B" :
#     print("Good")
# elif alp == "C" :
#     print("Usually")
# elif alp == "D" :
#     print("Effort")
# elif alp == "F" :
#     print("Failure")
# else :
#     print("error")

# 문제 7.
# 3개의 정수를 입력받아 조건문을 이용하여 입력받은 수들 중 최소값을 출력하는 프로그램을 작성하시오.
# 입력 예: 18 -5 10
# 출력 예: -5

# A = int(input("정수를 입력하시오."))
# B = int(input("정수를 입력하시오."))
# C = int(input("정수를 입력하시오."))

# if A>C and B>C :
#     print(C)
# elif B > A and C > A :
#     print(A) 
# else  :
#     print(B)


# 문제 8.
# 년도를 입력받아 윤년(leap year)인지 평년(common year)인지 판단하는 프로그램을 작성하시오.
# 400으로 나누어떨어지면 윤년이다. 또는 4로 나누어떨어지고 100으로 나누어떨어지지 않으면 윤년이다. 나머지는 모두 평년이다.
# 입력 예: 2008
# 출력 예: leap year

# year = int(input("년도를 입력하시오."))

# if year%4 == 0 :
#     print("leap year")
# else :
#     print("common year")

# 문제 9.
# 1~12사이의 정수를 입력받아 평년의 경우 입력받은 월을 입력받아 평년의 경우 해당 월의 날수를 출력하는 프로그램을 작성하시오.
# 평년의 경우 1월부터 12월까지 일수는 각각 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31일이다.
# 입력 예: 2
# 출력 예: 28

# month = int(input("월을 입력하시오."))

# if month == 1 or month ==3 or month ==5 or month ==7 or month ==8 or month ==10 or month ==12:
#     print(31)
# elif month == 4 or month ==6 or month ==9 or month ==11 :
#     print(30)
# else :
#     print(28)

# 문제 10.
# 공백을 포함한 문자열을 입력받아 각 단어로 분리하여 문자열 배열에 저장한 후 입력순서의 반대 순서로 출력하는 프로그램을 작성하시오. 문자열의 길이는 100자 이하이다.
# 입력 예: C++ Programing jjang!!
# 출력 예:
# jjang!!
# Programing
# C++

# letter = input("공백을 포함한 문자열을 입력하시오.")

# print(letter.split(" ")[::-1])