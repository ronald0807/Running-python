# 문제 6.
# 삼각형의 밑변의 길이와 높이를 입력받아 넓이를 출력하고, "Continue? "에서 하나의 문자를 입력받아 그 문자가 'Y' 나 'y' 이면 작업을 반복하고 다른 문자이면 종료하는 프로그램을 작성하시오.

word = "y"

while word == "y" or word == "Y" :
   
    if word == "Y" or word == "y" :
        base = int(input("밑변의 길이를 입력하시오."))
        height = int(input("높이를 입력하시오."))
        Trianglewidth = base * height /2 
    print(round(Trianglewidth,1))
    word = input("continue?")