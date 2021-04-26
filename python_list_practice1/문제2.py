
# 문제 2.
# 10개의 문자를 입력받아서 첫 번째 네 번째 일곱 번째 입력받은 문자를 차례로 출력하는 프로그램을 작성하시오.
# 입력 예: A B C D E F G H I J
# 출력 예: A D G

list = []

for i in range(10) :
    list.append(input("문자 10개를 입력하시오."))
print(list[0], list[3], list[6])
