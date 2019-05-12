ph = int(input("ph를 입력하시오.:"))

if ph>=0 and ph<=4:
    print("강산성")
elif ph>=5 and ph<=6:
    print("약산성")
elif ph==7:
    print("중성")
elif ph>=8 and ph<=9:
    print("약염기성")
elif ph>=10 and ph<=14:
    print("강염기성")
