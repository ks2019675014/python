s_even = 0
s_odd = 0

for i in range(1,101,1):
    if i % 2 ==0:
        s_even += i
    else:
        s_odd += i
        
print("홀수의 합: ", s_odd)
print("짝수의 합: ", s_even)
