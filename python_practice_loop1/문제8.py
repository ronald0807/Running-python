# 문제 8.(for)
# 두 개의 정수를 입력받아 두 정수 사이(두 정수를 포함)에 3의 배수이거나 5의 배수인 수들의 합과 평균을 출력하는 프로그램을 작성하시오.
# 평균은 반올림하여 소수 첫째자리까지 출력한다.
# 입력 예: 10 15
# 출력 예: sum : 37 avg : 12.3

num1 = int(input("첫번째 정수를 입력해주세요."))
num2 = int(input("두번째 정수를 입력해주세요."))
sum = 0
count = 0
avg = 1
for i in range (num1, num2+1) :
    if i%3 == 0 or i%5 == 0 :
        sum = sum + i
        count = count + 1
        avg = sum/count
print("sum:", sum, "avg:", avg)