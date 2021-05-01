#변수는 저장공간
    #num=10
#리스트는 여러개의 변수를 저장하는 공간
    #list=[변수1,변수2,변수3~~]
#문제51
movie_rank=["닥터 스트레인지","스플릿","럭키"]
print(movie_rank)
#문제52
movie_rank=["닥터 스트레인지","스플릿","럭키"]
movie_rank.append("베트맨")
print(movie_rank)
#문제53
movie_rank=["닥터 스트레인지","스플릿","럭키","베트맨"]
movie_rank.insert(1,"슈퍼맨")
#문제54
movie_rank=["닥터 스트레인지","슈퍼맨","스플릿","베트맨"]
del movie_rank[3]
#문제55
movie_rank=["닥터 스트레인지","슈퍼맨","스플릿","베트맨"]
del movie_rank[2]
del movie_rank[2]
print(movie_rank)
#문제56
lang1=["C","C++","JAVA"]
lang2= ["Python","Go","C#"]
리스트 =lang1+lang2
print(리스트)
#문제57
nums=[1,2,3,4,5,6,7]
print(max(nums))
print(min(nums))
#문제58
nums=[1,2,3,4,5]
print(sum(nums))
#문제59
cook=["피자","김밥","만두","양념치킨","족발","피자","김치만두","쫄면","쏘세지","라면","팥빙수","김치전"]
print(len(cook))
#문제60
nums=[1,2,3,4,5]
평균=sum(nums)/len(nums)
print(평균)
