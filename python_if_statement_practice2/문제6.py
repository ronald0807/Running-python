
# 문제 6.
# 영어 알파벳 문자 하나를 입력받아 대소문자를 구분하는 코드를 작성하십시오.
# 입력 예1: 'A'
# 출력 예1: 대문자입니다.
# 입력 예2: 'h'
# 출력 예2: 소문자입니다.

letter = input("알파벳 하나를 입력하시오.")

capital = "ASDFGHJKLMNBVCXQWERTYUIOP"

if letter in capital :
    print("대문자입니다.")
else :
    print("소문자입니다.")