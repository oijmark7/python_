def solution(member_age, transportation):#함수정의
	if transportation == 'Bus':#교통수단이 버스라면
		adult_expense = 40000#어른 가격은 4만원
		child_expense = 15000#어린이 가격은 만 5천원
	elif transportation == 'Ship':#교통수단이 배라면
		adult_expense = 30000#어른 가격은 3만원
		child_expense = 13000#어린이 가격은 만 3천원
	elif transportation == 'Airplane':#교통수단이 비행기라면
		adult_expense = 70000#어른 가격은 7만원
		child_expense = 45000#어린이 가격은 4만 5천월

	if len(member_age) >= 10:#만약 10명이상이라면
		adult_expense = 0.9*adult_expense#어른 요금의 10프로할인
		child_expense = 0.8*child_expense#어린이 요금의 20프로할인


	total_expenses = 0#총 교통비용의 값을 0으로 설정
	for age in member_age:# 사람수만큼 반복하기
		if age>=20:#만약 나이가 20세 이상이라면
			total_expenses += adult_expense#어른요금을 총합계에 더하기
		else:#이 아니면
			total_expenses += child_expense#어린이교금을 총 합계에 더하기

	return total_expenses#반환하기


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
member_age1 = [13, 33, 45, 11, 20] #할인x#어른3 어린이2
transportation1 = "Bus"#교통수단은 버스
ret1 = solution(member_age1, transportation1)#함수실행

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")#출력하기

member_age2 = [25, 11, 27, 56, 7, 19, 52, 31, 77, 8]#할인# 어린이4 어른6
transportation2 = "Ship"#교통수단은 배
ret2 = solution(member_age2, transportation2)#함수실행

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")#출력하기