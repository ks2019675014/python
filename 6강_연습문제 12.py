s = 0
x = int(input("정수 입력:"))
while x != 0:
    x = int(input("정수 입력:"))
    s += x
    if x== 0:
        print ("sum:", s)
        break
