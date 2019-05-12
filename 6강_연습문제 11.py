for i in range (1,6):
    for k in range (1,6-i):
        print(" ", end = "")
    for j in range (1,1+i):
        print ("*", end ="")
    for o in range (1,i):
        print ("*", end = "")
    print("")
