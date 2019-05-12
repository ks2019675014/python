import sys
num = [8,7,3,2,9,4,1,6,5]
max_val= -sys.maxsize - 1
min_val= sys.maxsize

for value in num:
    if value > max_val:
        max_val = value
    if value < min_val:
        min_val = value


print("최댓값:" , max_val)
print("최솟값:" , min_val)
