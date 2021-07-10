def solution(name_list):#함수정의
    answer = 0#정답
    for name in name_list:#name_list만큼 반복
        for n in name:#name만큼 반복
            if n == 'j' or n == 'k':#만역 n에 j또는 k가 있다면
                answer += 1#정답에 1더하기
                break#반복중지
    return answer#정답반환



# def solution(name_list):
#     answer = 0
#     for name in name_list:
#         for n in name:
#             if n == 'j' or n == 'k':
#                 answer += 1
#                 break
#     return answer