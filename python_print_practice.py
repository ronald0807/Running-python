# 문제 1

# 다음 출력 예와 같이 출력되는 프로그램을 작성하시오.
# 합계와 평균은 수식을 이용하세요.
# 합계 : 세 과목의 총합
# 평균 : 세 과목의 평균
# 출력 예:
# kor 90
# mat 80
# eng 100
# sum 270
# avg 90

# 국어 = 90
# 수학 = 100
# 영어 = 80

# 총합 = 국어 + 수학 + 영어
# 평균 = 총합/3

# print(총합)
# print(평균)

# 문제 2

# 다음과 같이 출력되는 프로그램을 작성하라.
# 각 요소사이의 공백은 tab으로 구분.
# 출력 예:
# item count price
# pen 20 100
# note 5 95
# eraser 110 97


# print("item  count   price")
# print("chicken  2   10000")
# print("pizza    5   8000")
# print("coke     5   1000")


# 문제 3
# 두 개의 정수를 변수에 각각 담고, 다음과 같이 4가지 관계연산자의 결과를 출력하시오.
# 입력 예: 4 5
# 출력 예:
# 4 > 5 --- 0
# 4 < 5 --- 1
# 4 >= 5 --- 0
# 4 <= 5 --- 1 

# x= 6
# y= 9

# if x > y : 
#     print("x > y --- 1")
# else :
#     print("x > y --- 0")

# if x < y :
#     print("x < y --- 1")
# else :
#     print("x < y --- 0")
# if x >= y :
#     print("x >= y --- 1")
# else :
#     print("x >= y --- 0")
# if x <= y :
#     print("x <= y --- 1")
# else :
#     print("x <= y --- 0")


# 문제 4
# 두 변수에 논리 값(true, false)을 각각 임의로 대입하고, 논리 합(or)과 논리 곱(and)의 결과를 출력하시
# 오.
# 입력 예: False True
# 출력 예:
# 논리 합: False or True => True
# 논리 곱: False and True => False

# x = "True" 
# y = "False"

# if x or y :
#     print("True")
# else :
#     print("False")
# print(x and y)

# 문제 5
# 3개의 정수를 변수 3개에 담아 첫 번째 수가 가장 크면 True 아니면 False을 출력하고,
# 세 개의 수가 모두 같으면 True 아니면 False을 출력하는 프로그램을 작성하시오.
# 입력 예: 10 9 9
# 출력 예: True
#         False


# x = int(input("첫 번째 정수를 입력하시오."))
# y = int(input("두 번째 정수를 입력하시오."))
# z = int(input("세 번째 정수를 입력하시오."))

# if x >= y and x >= z :
#     print("True")
# else :
#     print("False")

# 문제 6

# 두 정수를 변수 2개에 각각 담고 나눈 몫과 나머지를 다음과 같은 형식으로 출력하는 프로그램을 작성하시
# 오.
# 입력 예: 35 10
# 출력 예:
# 35 / 10 = 3...5

# x = int(input("첫 번째 정수를 입력하시오."))
# y = int(input("두 번째 정수를 입력하시오."))

# print(x//y)
# print(x%y)


# 문제 7

# 직사각형의 가로와 세로의 길이를 정수형 값을 변수에 담고,
# 가로의 길이는 5 증가시키고 세로의 길이는 2배하여 저장한 후 가로의 길이 세로의 길이 넓이를 차례로 출
# 력하는 프로그램을 작성하시오.
# 입력 예: 20 15 (앞에 입력된 값이 가로, 뒤에 입력된 값이 세로 길이)
# 출력 예:
# width = 25
# length = 30
# area = 750

# x = int(input("직사각형의 가로의 길이를 적으시오"))
# y = int(input("직사각형의 세로의 길이를 적으시오"))

# xx = x + 5
# yy = 2 * y

# width = xx
# length = yy
# area = xx * yy

# print(width)
# print(length)
# print(area)

# 문제 8

# 민수와 기영이의 키와 몸무게를 각각 변수에 담고, 민수가 키도 크고 몸무게도 크면 True 그렇지 않으면
# False을 출력하는 프로그램을 작성하시오.
# 입력 예:
# 150 35 (민수의 키와 몸무게 값)
# 145 35 (가영이의 키와 몸무게 값)
# 출력 예: False

# 민수의키 = int(input("민수의 키를 입력하시오."))
# 민수의몸무게 = int(input("민수의 몸무게를 입력하시오."))

# 기영이의키 = int(input("기영이의 키를 입력하시오."))
# 기영이의몸무게 = int(input("기영이의 몸무게를 입력하시오."))

# if 민수의키 > 기영이의키 and 민수의몸무게 > 기영이의몸무게 :
#     print("Ture")
# else :
#     print("False")