

# 문제 2.
# 자연수 n을 입력받아 "출력 예"와 같이 공백으로 구분하여 출력하는 프로그램을 작성하시오.
# 입력 예: 3

n = int(input("자연수를 입력하시오."))

for i in range(1,n+1) :
    print(" "*(n-i), end =" ")
    for j in range (1, i+1) :
        print(j, end=" ")
    print()
