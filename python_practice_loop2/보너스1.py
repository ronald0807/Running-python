#  보너스
# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최소값을 찾는 프로그램을 작성하시오.
# 예를 들어 M=60, N=100이 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로,
# 이들 소수의 합은 620이고, 최소값은 61이 된다.

def numberOfPrime(M,N) :
    result = []
    for i in range(M,N+1) :
        num = 0
        for j in range(1, i+1) :
            if i%j == 0 :
                num += 1
        if num == 2 :
            result.append(i)
    return result


M = int(input("자연수를 입력하시오."))
N = int(input("자연수를 입력하시오."))


print(sum(numberOfPrime(M,N)))
print(min(numberOfPrime(M,N)))