def solution(s):#함수정의
    s_lst = list(s)#s_list를 list(s)로 정의
    n = len(s)#n은 s의 변수의 갯수만큼의 크기
    for i in range(n):#n의 변수의 갯수만큼 i에 대입
        if s_lst[i] == 'a':#만약 s_lst[i]가 a하면
            s_lst[i] = 'z'#z로 바꾸기
        elif s_lst[i] == 'z':#만약 z라면
            s_lst[i] =  'a'#a로바꾸기
    return "".join(s_lst)#정답 반환

# def solution(s):
#     s_lst = list(s)
#     n = len(s)
#     for i in range(n):
#         if s_lst[i] == 'a':
#             s_lst[i] = 'z'; continue
#         if s_lst[i] == 'z':
#             s_lst[i] =  'a'
#     return "".join(s_lst)