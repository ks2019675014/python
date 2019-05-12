x= input("키(cm)를 입력해주세요 : ")
y= input("몸무게(kg)를 입력해주세요 : ")
bmi = "y/(x*x)"
print("키(cm):",x)
print("몸무게(kg):",y)
if bmi<"18.5":
    print("저체중")    
elif bmi>="18.5" and bmi<"23":
    print("정상")
elif bmi>="23" and bmi<"25":
    print("과체중")   
elif bmi>="25" and bmi<"30":
    print("경도 비만")
elif bmi>="30" and bmi<"35":
    print("중등도 비만")
elif bmi>="35":
    print("고도 비만")
    
