#문제4:글자길이가 5이상인 단어를 이어 출력하기]
    #len(문자):문자의 길이
def solution(words):
    answer=""
    for word in words:#단어목록 내 단어를 하나씩 단어에 대입 반복
        if len(word)>=5:#단어길이가 5이상이면
            answer+=word#결과에 단어 추가
    if len(answer)<1:#결과에 아무 단어가 없으면
        결과="empty"#empty넣기


    return answer







words=["my","favorite","color","is","violet"]

print("5글자 이상의 단어의 개수는 : ", solution(words))

words2= ["yes","i","am"]
print("5글자 이상의 단어의 개수는 : ", solution(words2))