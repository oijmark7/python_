#문제61 #price 변수에는 날짜와 증가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라.
price=['20180728',100,130,140,150,160,170]
print(price[1:])
    #[슬라이싱]= [1:] = 2번쨰값부터 끝까지
#문제62 # 슬라이싱을 사용해서 홀수만 출력하라
nums=[1,2,3,4,5,6,7,8,9,10]
print(nums[::2])
    #[슬라이싱] = [::2]= 0부터 2개씩 이동 = 0,2,4,6,8,10
    #[시작번호:끝번호:이동단위]
#문제 63 #슬라이싱을 사용해서 짝수면 출력하라
nums=[1,2,3,4,5,6,7,8,9,10]
print(nums[1::2])
    #[슬라이싱]=[1::2] = 1번째 값부터 2개씩 이동 = 1,3,5,7,9
#문제64 #슬라이싱을 사용해서 리스트와 숫자를 역 방향으로 출력하라
nums=[1,2,3,4,5]
print(nums[::-1])
    #[슬라이싱] = [::-1] = 뒤로이동
#문제 65 #interest 리스트에는 아래의 데이터가 바인딩 되어있다.
interest=['삼성전자','LG전자','Naver']
print(interest[0],interest[2])
#문제66 #interest 리스트에는 아래의 데이터가 바인딩되어 있다
interest=['삼성전자','LG전자','Naver','SK라이닉스','미래에셋대우']
print(" ".join(interest))
    #join 함수 :리스트 내 항목을 합칠떄 사용
#문제67 #interest 리스트에는 아래의 데이터가 바인딩 되어있다.
interest=['삼성전자','LG전자','Naver','SK라이닉스','미래에셋대우']
print("/".join(interest))
#문제68
interest=['삼성전자','LG전자','Naver','SK라이닉스','미래에셋대우']
print("\n".join(interest))
    #\n: 줄바꿈 제어문자 \t : 들여쓰기 제어문자
#문제69
string= "삼성전자/LG전자/Naver"
interest=string.split("/")
print(interest)
#문제 70 #리스트에 있는 값을 오른차순으로 정렬하세요
data=[2,4,3,1,5,10,9]
data.sort()
print(data)
data.sort()
print(data)
#내림차순
data.sort(reverse=True)
print(data)