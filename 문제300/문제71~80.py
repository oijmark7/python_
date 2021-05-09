#튜플:리스트와 거의 유사 []=> ()
    #단점: 튜플은 값을 바꿀수가 없다
    #튜플명(값1,값2,값3 == 등)
    #튜플명=값1,값2,값3==등
#문제71
my_variable=()#튜플생성
#문제72
movie_rank=("닥터 스트레인지","스플릿","럭키")
#문제73
my_tuple=(1)
print(type(my_tuple))
my_tuple=(1,)
print(type(my_tuple))
#문제74
#t=(1,2,3)
#t[0]='a'#0번째 순서의 값을 a로변환
    #오류 발생 이유 : 튜플값을 바꿀수가 없다
#문제75
t=1,2,3,4
print(type(t))
#문제76
#t=('a','b','c')
#t[0]='a'
    #오류 발생 이유 : 튜플은 값을 바꿀수가 없다
#문제77
interest=["삼성전자","LG전자","my_tuple"]
print(list(interest))
#문제78
interest["삼성전자","LG전자","SK Hynlx"]
print(tuple(interest))
#문제79
temp=('apple','banana','cake')
a,b,c=temp
print(a,b,c)
#문제80
data=tuple(range(2,100,2))
print(data)
    #range(시작값 , 끝값, 증가단위)