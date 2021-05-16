#문제151
리스트=[3,-20,-3,44]
for 변수 in 리스트:
    if 변수 < 0:
        print(변수)
#문제152
리스트=[3,199,23,44]
for 변수 in 리스트:
    if 변수%3==0:
        print(변수)
#문제153
리스트=[13,21,12,14,30,18]
for 변수 in 리스트:
    if 변수%3==0 and 변수<20:
        print(변수)
#문제154
리스트=["I","study","python","language","!"]
for 변수 in 리스트:
    if len(변수)>=3:
        print(변수)
#문제155
리스트=["A","b","c","D"]
for 변수 in 리스트:
    if 변수.isupper():
        print(변수)
#문제156
리스트=["A","b","c","D"]
for 변수 in 리스트:
    if 변수.islower():
        print(변수)
#문제157
리스트=['dog','cat','parrot']
for 변수 in 리스트:
    print(변수.capitalize())
#문제158
리스트=['hello.py','ex01.py','intro.hwp']
for 변수 in 리스트:
    분리=변수.split(".")
    print(분리[0])
#문제159
리스트=['intra.h','intra.c','define.h','run.py']
for 변수 in 리스트:
    분리=변수.split(".")
    if 분리[1]=="h":
        print(변수)
#문제160
리스트=['intra.h','intra.c','define.h','run.py']
for 변수 in 리스트:
    분리=변수.split(".")
    if 분리[1]=="h" or 분리[1]=="c":
        print(변수)