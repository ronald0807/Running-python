# 문제 6.
# 영문 대문자를 입력받아
# 'A'이면 “Excellent”,
# 'B'이면 “Good”,
# 'C'이면 “Usually”,
# 'D'이면 “Effort”,
# 'F'이면 “Failure”,
# 그 외 문자이면 “error” 라고 출력하는 프로그램을 작성하시오.
# 입력 예: B
# 출력 예: Good


alp = input("영문 대문자를 입력하시오.")

if alp == "A" :
    print("Excellent")
elif alp == "B" :
    print("Good")
elif alp == "C" :
    print("Usually")
elif alp == "D" :
    print("Effort")
elif alp == "F" :
    print("Failure")
else :
    print("error")