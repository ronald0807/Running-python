# 문제 3

# 문자열을 입력받고 정수를 입력 받아서 문자열의 맨 뒤부터 정수만큼 출력하는 프로그램을 작성하시오.
# 만약 입력받은 정수가 문자열의 길이보다 크다면 맨 뒤부터 맨 처음까지 모두 출력한다.
# 입력 예: korea 3
# 출력 예: aer

letter = input("문자열을 입력하시오.")
int = int(input("정수를 입력하시오."))

if len(letter) < int :
    print(letter[::-1])
else :
    print(letter[len(letter):int:-1])
