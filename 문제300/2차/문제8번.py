#문제8: 각 자리수열 소수 구라기 => 한줄변경
def solution(number):
    count= 0#자연수의 개수
    # while number>= 0:
    while number:
        n= number%10# 끝 한자리 구하기
        if n ==2 or n==3 or n== 5 or n== 7:
            # 끝 한자리가 2,3,5,7 이면 자연수
            count+=1#자연수 개수 증가
        number //=10#나머지 버리기
    return count



number =29022531# 29022531 %10 =>1
# 2902253%10=>3
# 290225%10=>5
ret = solution(number)

print("solution 실행 경과 값음 : ", ret)
print("ㅣnumberㅣreturnㅣ\nㅣ--------ㅣ------ㅣ\n","ㅣ",number,"ㅣ",ret,"ㅣ")
