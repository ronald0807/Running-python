# 문제 7.
# 가상의 두 사람(A, B)이 가위 바위 보 중 하나를 내서 승패를 가르는 가위 바위 보 게임을 작성하십시오.
# 이 때 ["가위", "바위", "보"] 리스트를 활용합니다.
# 입력 예: "가위" "바위"
# 출력 예: "B가 이겼습니다."

A = input("가위바위보를 하십시오.")
B = input("가위바위보를 하십시오.")

if (A =="가위" and B =="보") or (A =="보" and B =="바위") or (A == "바위" and B == "가위") :
    print("A가 이겼습니다.")
elif (A =="바위" and B =="보") or (A =="가위" and B =="바위") or (A == "보" and B == "가위") :
    print("B가 이겼습니다.")
else :
    print("비겼습니다. 다시 하십시오.") 
