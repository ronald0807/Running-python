# 문제 6.
# 10개의 정수를 입력받아 100 미만의 수 중 가장 큰 수와 100 이상의 수 중 가장 작은 수를 출력하는 프로그램을 작성하시오.
# 입력 예: 88 123 659 15 443 1 99 313 105 48
# 출력 예: 99 105

list = []
score1  = []
score2 = []

for i in range(10) :
    list.append(int(input("정수를 입력하시오.")))
    if list[i] >= 100 :
        score1.append(list[i])
    else :
        score2.append(list[i])
    
print(list)
print(min(score1))
print(max(score2))