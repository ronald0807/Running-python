

# 문제 8.
# 소수(prime number)란 1보다 큰 자연수 중 1과 자기 자신 두 개만을 약수로 갖는 수를 말한다.
# 자연수 M과 N을 입력받아 M부터 N까지 소수의 개수를 구하여 출력하는 프로그램을 작성하시오.
# M이상 N이하의 자연수 중 소수가 몇 개인지 구하여 출력한다.
# 입력 예: 10 100
# 출력 예: 21

def numberOfPrime(M,N) :
    result = 0
    for i in range(M,N+1) :
        num = 0
        for j in range(1, i+1) :
            if i%j == 0 :
                num += 1
        if num == 2 :
            result += 1
    return result

M = int(input("자연수를 입력하시오."))
N = int(input("자연수를 입력하시오."))

print(numberOfPrime(M,N))


