





# 문제 8.
# 다음의 결과와 같이 입력된 문자가 대문자일 경우 소문자로, 소문자일 경우 대문자로 변경하고,
# 알파벳이 아닐 경우엔 그냥 출력하는 코드를 작성하십시오.
# 입력 예1: A
# 출력 예1: a
# 입력 예2: 가나다
# 출력 예2: 가나다




letter = input("문자를 입력하시오.:")

capital = "ASDFGHJKLMNBVCXCZQWERTYUIOP"
small = "asdfghjklzxcvbnmqwertyuiop"

if letter in capital :
    print(letter.lower())
elif letter in small :
    print(letter.upper())
else :
    print(letter)
