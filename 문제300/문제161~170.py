#문제161
for i in range(100):
    print(i)
#문제162
for i in range(2002,2051,4):
    print(i)
#문제163
for i in range(3,31,3):
    print(i)
#문제164
for i in range(99,-1,-1):
    print(i)
#문제165
for i in range(0,10,1):
    print(i/10)
#문제166
for 곱 in range(1,10):
    print(3,"x",곱,"=",3*곱)
#문제167
for 곱 in range(1,10):
    if 곱%2 ==1 :
        print(3,"x",곱,"=",3*곱)

#홀수/ 짝수 구하기
#값%2==0: 해당값은짝수
#값%2==1: 해당값은홀수
#배수 구라기
#값%수==0: 나머지가 0이면 값은 그의 수의 배수
#문제168
합계=0
for 변수 in range(1,11):
    합계 += 변수

print("누적합계:",합계)
#문제169
합계 =0
for 변수 in range(1,11):
    if 변수%2==1:
        합계+=변수

#문제170
누적곱=1
for 변수 in range(1,11):
    누적곱 *= 변수
print("누적곱:",누적곱)