def solution(scores):
    grade_counter = [0 for i in range(5)]#리스트 생성
    for x in scores:#스코어 수만큼 반복
        if 85<=x and x<=100:#85점이상 100점 이하일경우
            grade_counter[0] += 1#A
        elif 70<=x and x<=84:#70점 이상 84점 이하일경우
            grade_counter[1] += 1#B
        elif 55<=x and x<=69:#55점 이상 69점이하일경우
            grade_counter[2] += 1#C
        elif 40<=x and x<=54:#40점이상 54점 이하일경우
            grade_counter[3] += 1#D
        else:#아니면
            grade_counter[4] += 1#E
    return grade_counter#담반환

# def solution(scores):
#     grade_counter = [0 for i in range(5)]
#     for x in scores:
#         if x >= 85:
#             grade_counter[0] += 1
#         elif x >= 70:
#             grade_counter[1] += 1
#         elif x >= 55:
#             grade_counter[2] += 1
#         elif x >= 40:
#             grade_counter[3] += 1
#         else:
#             grade_counter[4] += 1
#     return grade_counter
