#연산자:
    #산술연산자:+더하기-빼기*곱하기/나누기//나누기(몫)%나누기(나머지)**(제곱)
    #비교연산자:>초과<미만>=이상<=이하 ==같다 !=같지않다
    #논리연산자:and[이면서]or [이거나] ![부정]
    #대입연산자:=[오른쪽값을 왼쪽에대입]
                #+= [오른쪽값을 왼쪽값에 더하기후 왼쪽값에 대입]
                #-= [오른쪽값을 왼쪽값에 빼기 후 왼쪽값에 대입]
                #*= /= %=등
    #IF :논리문

    #   IF 논리:
    #       참[코드]
    #   else:
    #       거짓[코드]

    #if 논리:
    #    참[코드]
    #elif 논리2:
    #    참2[코드]
    #elif 논리3:
    #    참3[코드]
    #else:
    #    거짓[코드]

    #if 논리:
    #    참[코드]
    #if 논리2:
    #    참2[코드]
    #if 논리3:
    #    참3[코드]

    #if 논리:
    #   if 논리:
    #       참[코드]
    #   else:
    #       거짓[코드]
    #else:
    #   if 논리:
    #       참[코드]
    #   else:
    #       거짓[코드]

#문제101: type(): 데이터의 타입[형태] 확인해주는 함수
print(type(True))#bool : 참[True] 거짓[False] 둘중 하나 저장하는 함수
print(type(False))#bool : 참[True] 거짓[False] 둘중 하나 저장하는 함수

#문제102
print(3==5)#3과 5는 같은가? False
#문제103
print(3<5)#3은 5보다 미만인가? True
#문제104
x=4
print(1<x<5)# x은 1보다 초과이고 5보다 미만인가? True
#문제105:
print((3==3)and (4!=3))#3과 3은 같다 이면서 4와 3은 다른가? True
    #true 이면서 true=true
    #true 이면서 false = false
#문제106
#print(3=>4)오류발생이유 : 같거나 초과 기호는 없음 // 초과나 같다 >=[이상]

#문제107
if 4<3 : #false
    print("hello World")# True가 아니기 때문에 출력되지 않음
#문제108
if 4<3: #false
    print("Hello World")#출력되지 않음
else:#거짓이면
    print("HI,there")#4<3 false 이기 때문에 출력
#109
if True:#True 이면 실행
    print("1")#출력
    print("2")#출력
else:
    print("3")#출력되지않음
print("4")#if 절과 관련없는 함수 이므로 출력됨
#110
if True:#실행
    if False:#실행x
        print("1")#출력x
        print("2")#출력x
    else:#실행
        print("3")#출력
else:
    print("4")
print("5")#if와 관련없는 수 이므로 출력