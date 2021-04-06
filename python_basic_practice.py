# 문제 1
# 1야드(yd)는 91.44cm이고 1인치(in)는 2.54cm이다.
# 2.1야드와 10.5인치를 각각 cm로 변환하여 다음 형식에 맞추어 소수 첫째자리까지 출력하시오.
# 출력 예:
# 2.1yd = 192.0cm
# 10.5in = 26.7cm

# yd = 91.44
# 인치 = 2.54
# print(round(2.1 * yd,1),"cm")
# print(round(10.5 * 인치,1), "cm")

# 문제 2

# 문자열을 입력받은 뒤 그 문자열을 이어서 두 번 출력하는 프로그램을 작성하시오.
# 문자열의 길이는 100이하이다.
# 입력 예: ASDFG
# 출력 예: ASDFGASDFG

#print("asdfgo"*10)


# 문제 3

# 문자열을 입력받고 정수를 입력 받아서 문자열의 맨 뒤부터 정수만큼 출력하는 프로그램을 작성하시오.
# 만약 입력받은 정수가 문자열의 길이보다 크다면 맨 뒤부터 맨 처음까지 모두 출력한다.
# 입력 예: korea 3
# 출력 예: aer

# letter = input("문자열을 입력하시오.")
# int = int(input("정수를 입력하시오."))

# if len(letter) < int :
#     print(letter[::-1])
# else :
#     print(letter[len(letter):int:-1])

# 문제 4

# 단어와 문자 한 개를 입력받아서 단어에서 입력받은 문자와 같은 문자를 찾아서 그 위치를 출력하는 프로
# 그램을 작성하시오.
# 입력 예: Jungol.co.kr o
# 출력 예: 4

# letter = input("단어를 입력하시오")
# word = input("문자 하나를 입력하시오")

# print (letter.find(word))

# 문제 5

# 문자열(100자 이하)을 입력받은 후 정수를 입력받아 해당위치의 문자를 제거하고 출력하는 프로그램을
# 작성하시오.
# 입력 예1: word 3 출력 예: wod

# letter = input("문자를 입력하시오.")
# int = int(input("정수를 입력하시오:"))

# letter2 = letter.replace(letter[int],"")
# print(letter2)

# 문제 6

# 20개 이하의 문자로 이루어진 10개의 단어와 한 개의 문자를 입력받아서 마지막으로 입력받은 문자로 끝
# 나는 단어를 모두 출력하는 프로그램을 작성하시오.
# 입력 예:
# champion
# tel
# pencil
# olympiad
# class
# information
# jungol
# lesson
# book
# lion
# l <<<<알파벳 엘입니다.

# letter1 = input("문자를 입력하시오")
# letter2 = input("문자를 입력하시오")
# letter3 = input("문자를 입력하시오")
# letter4 = input("문자를 입력하시오")
# letter5 = input("문자를 입력하시오")

# list = ["letter2","letter3","letter1","letter4","letter5"]

# if "l" in list:
#     print(list)

# 문제 7
# 두 개의 문자열 A와 B 한 개의 정수 n을 입력받아서 A에 B를 연결하고, 변경된 문자열 A에서 n개의 문자
# 를 B에 복사한 후 A와 B를 출력하는 프로그램을 작성하시오. (1≤n,A,B≤100)
# 입력 예: banana apple 3
# 출력 예:
# bananaapple
# banle
# 입력 예2: orange watermelon 5
# 출력 예2:
# orangewatermelon
# orangmelon


# A = input("문자를 입력하시오.")
# B = input("문자를 입력하시오.")
# n = int(input("정수를 입력하시오."))
# C = A+B

# print(C)

# print(C[n:n+n:1])



