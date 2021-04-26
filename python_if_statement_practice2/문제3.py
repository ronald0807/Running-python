# 문제3.
# 초를 입력 받아서 시간과 분으로 변환하는 프로그램을 작성하시오.
# 입력 예: 3598
# 출력 예: 59분 58초

sec = int(input("초를 입력하시오."))

if sec // 3600 >= 1 :
    hr = sec // 3600
    min = (sec%3600)//60
    sec2 = sec - hr*3600 - min*60
    print(hr,"시", min,"분", sec2,"초", sep="")
elif sec // 60 >= 1 :
    min = (sec//60)
    sec2 = sec - min*60
    print(min, "분", sec2,"초",sep="")
else :
    print(sec,"초",sep="")
