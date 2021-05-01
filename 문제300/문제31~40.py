#문제31
a="3"
b="4"
print(a+b)
#문제 32
print("HI"*3)
#문제33:-[하이폰]
print("-"*80)
#문제34
t1='python'
t2='java'
t3= t1+ " " + t2 + " "
print(t3*4)
#문제35
name1="김민수"
age1=10
name2="이철희"
age2=13
print("이름:%s 나이:%d" %(name1,age1) )
print("이름:%s 나이:%d" %(name2,age2) )
#문제36
name1="김민수"
age1=10
name2="이철희"
age2=13
print("이름:{} 나이:{}".format(name1,age1) )
print("이름:{} 나이:{}".format(name2,age2) )
#문제37
name1="김민수"
age1=10
name2="이철희"
age2=13
print(f"이름:{name1} 나이:{age1}"  )
print(f"이름:{name2} 나이:{age2}" )
#문제38
상장주식수="5,969,782,550"
컴마제거 = 상장주식수.replace(",","")
타입변환 = int(컴마제거)
print(타입변환)
#문제39
분기="2020/03(E)(IFRS연결)"
print(분기[0:7])
#문제40
data="          삼성전자            "
공백제거=data.strip()
print(공백제거)