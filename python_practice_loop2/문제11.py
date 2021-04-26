# 문제 11.
# 2진수를 입력받아 10진수로 변환하여 출력하는 프로그램을 작성하시오.
# 입력 예: 10101
# 출력 예: 21

n = str(input("2진수를입력하세요."))
result = 0
for i  in range(len(n)) :
    if i == len(n) -1   :
        if n[i] == "1" :
            result += 1 
    else :
        if n[i] == "1" :
            result = result + (2**((len(n)-1)-i))
print(result)
