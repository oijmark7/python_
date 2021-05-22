#문제191
data=[[200,3050,2050,1980],[7500,2050,2050,1980],[15450,15050,15550,14900]]
for 행 in data:
    for 열 in 행:
        print(열*1.00014)
#문제192
data=[[200,3050,2050,1980],[7500,2050,2050,1980],[15450,15050,15550,14900]]

for 행 in data:
    for 열 in 행:
        print(열*1.00014)
    print("-"*45)
#문제193
결과=[]
for 행 in data:
    for 열 in 행:
        결과.append(열*1.00014)
print(결과)
#문제194
결과=[]
for 행 in data:
    sub=[]
    for 열 in 행:
        sub.append(sub)
    결과.append(sub)
print(결과)
#문제195
ohlc=[["open","high","low","close"],[100,110,70,100],[200,210,180,190],[300,310,300,310]]
for 행 in ohlc[1:]:
    print(행[3])
#문제196
ablc=[["open","high","low","close"],[100,110,70,100],[200,210,180,190],[300,310,300,310]]
for 행 in ohlc[2:]:
    print(행[3])
#문제197
ablc=[["open","high","low","close"],[100,110,70,100],[200,210,180,190],[300,310,300,310]]
for 행 in ohlc[1::2]:
    print(행[3])
#문제198
변동폭=[]
for 행 in ohlc[1:]:
    변동폭.append(행[1]-행[2])
print(변동폭)
#문제199
for 행 in ohlc:
    if 행[3]>행[0]:
        print(행[1]-행[2])
#문제200
총수익금 = 0
for 행 in ohlc[1:]:
    총수익금+=(행[3]-행[0])
print(총수익금)
