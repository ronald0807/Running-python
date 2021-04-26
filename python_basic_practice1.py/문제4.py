# 문제 4

# 단어와 문자 한 개를 입력받아서 단어에서 입력받은 문자와 같은 문자를 찾아서 그 위치를 출력하는 프로
# 그램을 작성하시오.
# 입력 예: Jungol.co.kr o
# 출력 예: 4

letter = input("단어를 입력하시오")
word = input("문자 하나를 입력하시오")

print (letter.find(word))