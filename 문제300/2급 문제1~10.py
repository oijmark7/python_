#문제1

def solution( shirt_size ):

    size_count = [ 0 , 0 , 0 , 0 , 0 , 0 ]

    for ss in shirt_size :
        if ss =="XS":
            size_count[0] +=1
        if ss =="S":
            size_count[1] +=1
        if ss =="M":
            size_count[2] +=1
        if ss =="L":
            size_count[3] +=1
        if ss =="XL":
            size_count[4] +=1
        if ss =="XXL":
            size_count[5] +=1
    return size_count

shirt_size=["XS","S","L","L","XL","S"]
ret = solution(shirt_size)
print("solution : return value of the function is " , ret , " .")
#문제2
def solution(price, grade):
    answer=0

    if grade =="S":
        answer = price*0.95
    if grade =="G":
        answer = price*0.9
    if grade =="V":
        answer = price*0.85
    return int(answer)
price1=2500
grade1="V"
ret1=solution(price1,grade1)
print("Solution : return value of the function if",ret1," .")
price2=96900
grade2="S"
ret2= solution(price2,grade2)
print("Solution : return value of the function if",ret2," .")
#문제3
def func_a(month, day):
    month_list = [31, 28 ,31 ,30 ,31,30 ,31 , 31,30, 31,30,31]
    total = 0;
    for i in range(month-1):
        total += month_list[i]
    total +=day
    return total - 1
def solution(start_month,start_day,end_month,end_day):
    start_total = func_a(start_month,start_day)
    end_total = func_a(end_month,end_day)
    return end_total-start_total

start_month=1
start_day=2
end_month=2
end_day=2
ret=solution(start_month,start_day,end_month,end_day)
print("solution: return balue of the function is",ret," .")

#문제4
def func_a(arr):
    counter= [0 for _ in range(1001)]
        #자연수들 마다 개수를 저장하는 리스트
    for x in arr:#리스트 반복
        counter[x] +=1 #각 자연수 위치 인덱스에+1
    return counter
def func_b(arr):#2단계 함수 : 가장 많이 등장하는 수 세기
    ret=0#가장 많은 개수 가지고 있는 자연수를 찾아서 저장하는 변수
    for x in arr:
        if ret == "x" : #현재 가장큰 자연수보다< 헤당 자연수가 더 많으면
            ret = x#해당 자연수가 가장 큰 자연수가 된
        return  ret
def func_c(arr):# 3단계 함수: 가장 적게 등장하는 수 세기
    INF =1001
    ret=INF
    for x in arr:
        if x !=0 and ret>x:
            ret=x
        return ret
def solution(arr):
    counter =func_a(arr)
    max_cnt =func_b(counter)
    min_cnt =func_c(counter)
    return  max_cnt//min_cnt

arr = [1,2,3,3,1,3,3,2,3,2]
ret= solution(arr)

print("Solution: return value of the function is",ret," .")

#문제5

def solution(arr):
    left, right = 0,len(arr)-1
    #왼쪽=0 오른쪽=0 숫자갯수
    while left<right:#오른쪽이 더 클 경우에만
        arr[left],arr[right]=arr[right],arr[left]
        #첫번쨰 값[왼],처번째값[오른쪽]=첫번쨰값[오른쪽],첫번째값[왼쪽]
        left+=1#왼쪽 1증가
        right -=1#오른쪽 1감소
    return arr

    #left 0 일 경우 right 0=> 반복문실행
        #arr[0],arr[0]=arr[0],arr[0]
         #1     #1      #1     #1
        #left+1 right-1
    #left 1일 경우 right -1
        #arr[1],arr[-1]=arr[-1],arr[1]
          #4     #3         #3    #4
        #left+1    right-1
    #left 2 일경우 right-2
        #arr[2],arr[-2]= arr[-2],arr[2]
          #2       2  =   2       2
arr = [1,4,2,3]
ret=solution(arr)
print("Solution : return value of the function is",ret," .")

#문제6
def solution(number):
    count = 0#박수횟수
    for i in range(1, number+1):#1부터 40까지 반복
        current=i#반복숫자
        temp= count#임시변수에 박수횟수 저장
        while current != 0:#0이 아닐떄까지 반복
            if current%10==3 or current%10==6 or current%10==9:
                #만약에 현재 숫자가 나누기 10을 했을떄 나머지가 3혹은 6혹은 9이면
                count +=1#박수 횟수 올리기
                print("pair",end='')#박수 출력
            current =current//10#현재 숫자//10 자릿수 내리기
        if temp ==count:
            print(i,end='')
        print(" ",end=' ')
    print("")
    return  count
number=40
ret=solution(number)


print("Solution : return value of the function is",ret," .")