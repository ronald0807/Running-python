# 문제 3.
# 빈 리스트을 선언하고 정수를 차례로 입력받다가 0 이 입력되면 0 을 제외하고 그 때까지 입력된 정수를 가장 나중에 입력된 정수부터 차례대로 출력하는 프로그램을 작성하시오.
# 입력 예:
# 3
# 5
# 10
# 55
# 0
# 출력 예: 55 10 5 3

list = []
n = 1 

while n != 0 :
    n = int(input("정수를 입력하세요."))
    if n != 0 :
        list.append(n)
    
print(list[::-1])