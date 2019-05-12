x= int(input("1차 시험의 점수를 입력하시오: "))
y= int(input("2차 시험의 점수를 입력하시오: "))

if x>=60 and y>=60 and (x+y)/2>=60:
    print("축하합니다! 합격입니다!")


else:
    print(" 수고하셨습니다. 불합격입니다.")
