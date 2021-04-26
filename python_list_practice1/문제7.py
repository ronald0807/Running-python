# 문제 7.
# 10개의 정수를 입력받아 리스트에 저장한 후 짝수 번째 입력된 값의 합과 홀수 번째 입력된 값의 평균을 출력하는 프로그램을 작성하시오.
# 평균은 반올림하여 소수첫째자리까지 출력한다.
# 입력 예: 95 100 88 65 76 89 58 93 77 99
# 출력 예:
# sum : 446
# avg : 78.8

list = []
sum = 0
count = 0
for i in range(10):
    list.append(int(input("정수를 입력하세요.")))
    count += 1
    sum += list[i]
avg = sum / count
print(round(avg,1))
