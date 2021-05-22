

#1.for 변수 in 리스트명:
#2.for 변수 range(시작값, 끝값,증가단위):
#3.for 변수 in enumerater(리스트명): 인덱그와 값 동시변환

#문제171
price_list=[32100,32150,32000,32500]
for i in range(0,4):
    print(price_list[i])
#문제172
price_list=[32100,32150,32000,32500]
for i,변수 in enumerate(price_list):
    print(i,변수)
#문제173
price_list=[32100,32150,32000,32500]
for i in range(3,-1,-1):
    print(i,price_list[i])
#문제174
price_list=[32100,32150,32000,32500]
for i in range(1,4):
    print(90+10*i,price_list[i])
#문제175
my_list=["가","나","다","라"]
for i in range(0,3):
    print(my_list[i],my_list[i+1])
#문제176
my_list=["가","나","다","라","마"]
for i in range(0,3):
    print(my_list[i],my_list[i+1],my_list[i+2])
#문제177
my_list=["가","나","다","라"]
for i in range(3,0,-1):
    print(my_list[i], my_list[i - 1])
#문제178
my_list=[100,200,400,800]
for i in range(0,3):
    print(my_list[i+1]-my_list[i])
#문제179
my_list=[100,200,400,800,1000,1300]
for i in range(0,4):
    print((my_list[i]+my_list[i+1]+my_list[i+2])/3)

#문제180
low_prices=[100,200,400,800,1000]
high_prices=[150,300,430,880,1000]
저장리스트=[]
저장리스트.append(high_prices[1]-low_prices[1])