#You may use import as below.
#import math

def solution(shirt_size):
    size=[0,0,0,0,0,0]
    for i in shirt_size:
        if i == "XS":
            size[0]+=1
        elif i == "S":
            size[1] += 1
        elif i == "M":
            size[2]+=1
        elif i == "L":
            size[3]+=1
        elif i == "XL":
            size[4]+=1
        elif i == "XXL":
            size[5]+=1


    answer = size
    return answer

#The following is code to output testcase.
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size);

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")