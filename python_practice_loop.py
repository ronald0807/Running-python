# 문제 1.(for)
# for 문을 이용하여 1부터 입력받은 정수까지의 합을 구하여 출력하는 프로그램을 작성하시오.
# 100 이하의 양의 정수만 입력된다.
# 입력 예: 10
# 출력 예: 55

# num = int(input("정수를 입력하시오."))
# sum = 0
# for i in range (1, num+1) :
#     sum = sum + i  # sum += i 
# print(sum)

# 문제 2.
# 정수를 계속 입력받다가 100 이상의 수가 입력이 되면 마지막 입력된 수를 포함하여 합계와 평균을 출력하는 프로그램을 작성하시오.
# 평균은 반올림하여 소수 첫째자리까지 출력한다.

# sum = 0
# count = 0
# x = 1 
# while x < 100 :
#     x = int(input("정수를 입력하시오."))
#     sum = sum + x 
#     count += 1 
#     avr = sum / count
# print("평균은", round(avr,1))

# 문제 3.
# 정수를 입력받아서 3의 배수가 아닌 경우에는 아무 작업도 하지 않고, 3의 배수인 경우에는 3으로 나눈몫을 출력하는 작업을 반복하다가 -1이 입력되면 종료하는 프로그램을 작성하시오

# num = 1

# while num != -1 :
#     num = int(input("정수를 입력하시오."))
#     if num % 3 == 0 :
#         print(num//3)
#     else :
#         print(num)

# 보너스(for)
# 아래와 같은 모양으로 출력하는 프로그램을 작성하시오.
# 사용자에게 숫자를 입력받아 입력 받은 높이 만큼의 삼각형을 출력하시오.
# 입력 예: 5

# height = int(input("높이를 입력하시오."))
# sum = ""
# for i in range (1,height+1):
#     sum = sum + "*"
#     print(sum)

# 문제 4.
# 아래와 같이 나라 이름을 출력하고 숫자를 입력받아 해당하는 나라의 수도를 출력하는 작업을 반복하다가 해당하는 번호 이외의 숫자가 입력되면 "none"라고 출력한 후 종료하는 프로그램을 작성하시오.
# 각 나라의 수도 :
# 대한민국 = 서울(Seoul)
# 미국 = 워싱턴(Washington)
# 일본 = 동경(Tokyo)
# 중국 = 북경(Beijing)
# 예시 입력 예:

# Korea
# USA
# Japan
# China number? 1
# 출력 예: Seoul

# Korea
# USA
# Japan
# China number? 5

# nation = ["Korea","USA","Japan","China"]
# capital = ["Seoul","Washington","Tokyo","Beijing"]
# num = 7
# while num > 0 :
#     num = int(input("숫자를 입력하시오."))
#     if num < 5 :
#         print(nation[num-1],capital[num-1])
#     else :
#         print("none")

# 문제 5.
# 0 이상의 정수들이 공백으로 구분되어 반복적으로 주어진다. 0이 입력되면 반복문을 멈추고 그 전까지 입력받은 수들에 대하여 홀수의 개수와 짝수의 개수를 출력하는 프로그램을 작성하시오.
# 입력 예: 9 7 10 5 33 65 0
# 출력 예: odd : 5 even : 1

# num = 100
# oddCount = 0
# evenCount = 0
# while num != 0 :
#     num = int(input("정수를 입력하시오.:"))
#     if num % 2 == 1 :
#         oddCount += 1
#     elif num == 0 :
#         num == 0
#     else :
#         evenCount += 1 
# print("odd:",oddCount,"even:", evenCount,)
    
# 문제 6.
# 삼각형의 밑변의 길이와 높이를 입력받아 넓이를 출력하고, "Continue? "에서 하나의 문자를 입력받아 그 문자가 'Y' 나 'y' 이면 작업을 반복하고 다른 문자이면 종료하는 프로그램을 작성하시오.

# word = "y"

# while word == "y" or word == "Y" :
   
#     if word == "Y" or word == "y" :
#         base = int(input("밑변의 길이를 입력하시오."))
#         height = int(input("높이를 입력하시오."))
#         Trianglewidth = base * height /2 
#     print(round(Trianglewidth,1))
#     word = input("continue?")

# 문제 7.(for)
# 100 이하의 두 개의 정수를 입력받아 작은 수부터 큰 수까지 차례대로 출력하는 프로그램을 작성하시오.
# 입력 예: 5 10
# 출력 예: 5 6 7 8 9 10

# num1 = int(input("첫번째 정수를 입력해주세요."))
# num2 = int(input("두번째 정수를 입력해주세요."))

# for i in range(num1,num2+1) :
#     print(i, end= " ")

# 문제 8.(for)
# 두 개의 정수를 입력받아 두 정수 사이(두 정수를 포함)에 3의 배수이거나 5의 배수인 수들의 합과 평균을 출력하는 프로그램을 작성하시오.
# 평균은 반올림하여 소수 첫째자리까지 출력한다.
# 입력 예: 10 15
# 출력 예: sum : 37 avg : 12.3

# num1 = int(input("첫번째 정수를 입력해주세요."))
# num2 = int(input("두번째 정수를 입력해주세요."))
# sum = 0
# count = 0
# avg = 1
# for i in range (num1, num2+1) :
#     if i%3 == 0 or i%5 == 0 :
#         sum = sum + i
#         count = count + 1
#         avg = sum/count
# print("sum:", sum, "avg:", avg)

# 문제 9. (for)
# 2부터 9까지의 수 중 2개를 입력받아 입력받은 수 사이의 구구단을 출력하는 프로그램을 작성하시오.
# 단 반드시 먼저 입력된 수의 구구단부터 아래의 형식에 맞게 출력하여야 한다.
# 구구단 사이의 공백은 3칸이다.

# num1 = int(input("2부터 9까지의 수중 하나를 입력하시오."))
# num2 = int(input("2부터 9까지의 수중 하나를 입력하시오."))
# mul = 1
# for x in range (1,10):
#     for i in range(num2, num1-1,-1) :
#         mul = i * x
#         print(i,"*",x,"=",mul, end=" ")

# 보너스2 (for)
# 아래와 같은 모양으로 출력하는 프로그램을 작성하시오.
# 사용자에게 숫자를 입력받아 입력 받은 높이 만큼의 삼각형을 출력하시오.
# 입력 예: 5

# height = int(input("높이를 입력하시오."))

# while height != 0 :
#     for i in range (height,0,-1):
#         print(height*"*")
#         height = height -1
