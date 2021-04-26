

# 문제 7.
# 3개의 정수를 입력받아 조건문을 이용하여 입력받은 수들 중 최소값을 출력하는 프로그램을 작성하시오.
# 입력 예: 18 -5 10
# 출력 예: -5

A = int(input("정수를 입력하시오."))
B = int(input("정수를 입력하시오."))
C = int(input("정수를 입력하시오."))

if A>C and B>C :
    print(C)
elif B > A and C > A :
    print(A) 
else  :
    print(B)
