#문제121
입력저장=input("영문 입력:")
if 입력저장.islower():
    print(입력저장.upper())
else:
    print(입력저장.lower())
#문제122
정수 = int(input("정수 입력:"))
if 정수 >= 81:
    print("a들급")
elif 정수>=61:
    print("B등급")
elif 정수>=41:
    print("C등급")
elif 정수 >=21:
    print("D등급")
else:
    print("E등급")
#문제123
환율={"달러":1167,"엔":1.096,"유로":1268,"위안":171}
입력저장=input("금액과 통화명 입력:")
금액,통화명= 입력저장.split(" ")
print(int(금액)*환율[통화명],"원")
#문제124
숫자1=int(input("숫자1입력:"))
숫자2=int(input("숫자2입력:"))
숫자3=int(input("숫자3입력:"))
#정답1
print(max(숫자1,숫자2,숫자3))
#정답2
if 숫자1>숫자2 and 숫자1>숫자3:
    print(숫자1)
if 숫자2>숫자3 and 숫자2>숫자1:
    print(숫자2)
if 숫자3>숫자2 and 숫자3>숫자1:
    print(숫자3)

#문제125
핸드폰번호=input("핸드폰번호 입력:")
통신사번호 =핸드폰번호.split("-")[0]
if 통신사번호 == "011":
    print("당신은 SKT입니다")
if 통신사번호 == "016":
    print("당신은 KT입니다")
if 통신사번호 == "019":
    print("당신은 LGU입니다")
else:
    print("알수없습니다")

#문제126
우편번호=input("우편번호:")
우편번호= 우편번호[0:3]
if 우편번호 in ["010","011","012"]:
    print("강북구")
elif 우편번호 in ["013","014","015"]:
    print("도붕구")
else:
    print("노월구")
#문제127
주민번호 = input("주민등록번호:")
주민번호 = 주민번호.split("-")[1]
if 주민번호[0]== "1" or 주민번호[0]=="3":
    print("남자")
else:
    print("여자")
#문제128
주민번호 = input("주민등록번호:")
뒷자리=주민번호.split("-")[1]
if 0<=int(뒷자리[1:3])<=0:
    print("서울입니다")
else:
    print("부산입니다")
#문제129
주민번호=input("주민등록번호:")
계산1= int(주민번호[0])*2+ int(주민번호[1])*3+int(주민번호[2])*4+ int(주민번호[3] )*5+\
     int(주민번호[4] )*6 + int(주민번호[5]) *7 +int(주민번호[7] )*8 + int(주민번호[8] )*9 + \
    int(주민번호[9] )*2 + int(주민번호[10] )*3 + int(주민번호[11] )*4 + int(주민번호[12])*5
계산2=11-(계산1%11)
계산3=str(계산2)
if 주민번호[-1]==계산3[-1]:
    print("유효한 주민등록번호입니다")
else:
    print("유효하지 않은 주민등록 번호입니다")
#문제130
import requests
btc=requests.get("https://api.bithumb.com/public/ticker/").json()['data']
변동폭=int(btc["max_price"])-int(btc["min_price"])
시가=int(btc["opening_price"])
최고가=int(btc["max_price"])
if (시가+변동폭)> 최고가:
    print("상승장")
else:
    print("하락장")