# 문제 5
# 3개의 정수를 변수 3개에 담아 첫 번째 수가 가장 크면 True 아니면 False을 출력하고,
# 세 개의 수가 모두 같으면 True 아니면 False을 출력하는 프로그램을 작성하시오.
# 입력 예: 10 9 9
# 출력 예: True
#         False


x = int(input("첫 번째 정수를 입력하시오."))
y = int(input("두 번째 정수를 입력하시오."))
z = int(input("세 번째 정수를 입력하시오."))

if x >= y and x >= z :
    print("True")
else :
    print("False")
