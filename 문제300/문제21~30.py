#문제21
letters='python'
print(letters[0],letters[2])
#문제22
license_plate="24가 2210"
print(license_plate[-4:])#뒤에서부터 4개
print(license_plate[4:8])
#문제23
string="홀짝홀짝홀짝"
print(string[0:6:2])
#문제24
string="PYTHON"
print(string[::-1])
#문제25
phone_number ="010-1111-2222"
phone_number1=phone_number.replace("-"," ")
print(phone_number1)
#문제26
phone_number ="010-1111-2222"
phone_number1=phone_number.replace("-","")
print(phone_number1)
#문제27
url="https://sharebook.kr"
url_split=url.split(".")
print(url_split)
#문제28
#lang ="python"
#lang[0]= 'P' #이유: 문자열 일부분 수정불가
#print(lang)

#문제29
string="abcdfea345a32a"
string=string.replace("a","A")
print(string)
#30
string='abcd'
string.replace('b','B')
print(string)
#예상:aBcd
