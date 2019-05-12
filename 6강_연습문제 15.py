s= 1
n= 0
while True:
    n += 1
    s = s*2
    print(n, "번 접으면", s, "mm" )
    
    if s > 100000:
        print("횟수: ", n, "두께: ", s)
        break
    
