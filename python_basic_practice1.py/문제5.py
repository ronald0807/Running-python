# 문제 5

# 문자열(100자 이하)을 입력받은 후 정수를 입력받아 해당위치의 문자를 제거하고 출력하는 프로그램을
# 작성하시오.
# 입력 예1: word 3 출력 예: wod

letter = input("문자를 입력하시오.")
int = int(input("정수를 입력하시오:"))

letter2 = letter.replace(letter[int],"")
print(letter2)
