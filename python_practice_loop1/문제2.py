

# 문제 2.
# 정수를 계속 입력받다가 100 이상의 수가 입력이 되면 마지막 입력된 수를 포함하여 합계와 평균을 출력하는 프로그램을 작성하시오.
# 평균은 반올림하여 소수 첫째자리까지 출력한다.

sum = 0
count = 0
x = 1 
while x < 100 :
    x = int(input("정수를 입력하시오."))
    sum = sum + x 
    count += 1 
    avr = sum / count
print("평균은", round(avr,1))
