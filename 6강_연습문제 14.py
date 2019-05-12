s = 0
x = int(input("정수:"))
while True:
    x = int(input("정수:"))
    if x>0:
        s += x
    elif x<0:
        continue
    else:
        print("sum",s)
        break
