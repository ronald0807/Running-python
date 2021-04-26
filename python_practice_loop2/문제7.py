문제 7.
학생들의 점수를 입력을 받다가 0이 입력되면 그 때까지 입력받은 점수를 10점 단위로 구분하여 점수대별 학생 수를 출력하는 프로그램을 작성하시오.
1명도 없는 점수는 출력하지 않는다.
입력 예: 63 80 95 100 46 64 88 0

# def count_range(x,y) :
#     range_list = []
#     for i in range(len(score)) :
#         if score[i]< x and score[i] >= y :
#             range_list.append(score[i])
#     return len(range_list)

# score = []
# student = int(input("학생의 수를 입력하세요."))

# for i in range(student) :
#     score.append(int(input("점수를 입력하세요.")))


# count9 = count_range(100,90)
# count8 = count_range(90,80)
# count7 = count_range(80,70)
# count6 = count_range(70,60)
# count5 = count_range(60,50)
# count4 = count_range(50,40)
# count3 = count_range(40,30)
# count2 = count_range(30,20)
# count1 = count_range(20,10)
# count0 = count_range(10,0)

# if count0 != 0 :
#     print("0점대:",count0)
# if count1 != 0:
#     print("10점대:",count1)
# if count2 != 0:
#     print("20점대:", count2)
# if count3 != 0:
#     print("30점대:", count3)
# if count4 != 0:
#     print("40점대:", count4)
# if count5 != 0:
#     print("50점대:", count5)
# if count6 != 0:
#     print("60점대:", count6)
# if count7 != 0:
#     print("70점대:", count7)
# if count8 != 0:
#     print("80점대:", count8)
# if count9 != 0:
#     print("90점대:", count9)
# if score.count(100) != 0 :
#     print("100점:", score.count(100))