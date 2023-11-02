multiLine='''Life is too short
You need pyton'''
print(multiLine)
#엔터를 포함하는 여러 줄의 문자열을 저장하기 위해서는 '''를 사용하여 묶는다.

head='Python'
tail=" is fun!"
#문자열을 표현할때는 다른 언어와 달리 '를 사용해도 문자가 아닌 문자열을 입력할 수 있다.
print(head+tail)
print(head*2+tail)

print(len(head))
#len()으로 문자열의 길이를 구할 수 있다.
#이때 널 문자를 포함하지 않는다

indexing='Life is too short, You need Python'
print(indexing[0]+indexing[12]+indexing[-1])
#인덱스가 음수인 경우에는 뒤에서부터 센다.
print(indexing[0:4])
#문자열 슬라이싱의 경우 뒤의 숫자는 포함하지 않는다.
#추가로 문자열은 변경이 불가능한 자료형이다.

slicing='20231101Sunny'
date=slicing[:8]
weather=slicing[8:]

print(date)
print(weather)
#슬라이싱을 통해 하나의 문장을 나누어서 표현할 수 있다.

slicing=slicing[8:]+slicing[:8]
print(slicing)
#인덱스로 하나의 문자를 바꾸는건 에러가 발생하지만
#앞뒤를 슬라이싱으로 쪼개서 순서를 바꾸거나 문자를 추가, 수정할 수 있다.

number=3
print("I eat %d apples."%number)
day='three'

print("I ate %d apples %s days ago"%(number,day))
#'%'를 이용해 변수를 출력할 수 있다.

print('%10s'%'hi')
print('%-10s'%'hi')
#%와 s 사이에 숫자를 집어넣어 정렬할 방향과 공백이 들어갈 공간을 표현할 수 있다

print('%.4f'%3.141592)
print('%.3f'%3.141592)
print('%.3f'%3.142592)
print('%.2f'%3.141592)
#.뒤에 숫자를 붙여 소숫점 몇번째자리까지 표현할지 정할 수 있다.
#반올림은 앞자리의 수와 상관없이 5이상이면 올림한다.

print('I eat {0} apples'.format(3))
print('I eat {0} apples'.format(number))
#{#}으로 format이 가능하다

print('{0:<10}'.format('hi'))
#화살표 방향으로(<,>,^) 정렬시킬 수 있다.
print('{0:=^10}'.format('hi'))
#:뒤에 문자를 넣어 공백을 채울 수 있다.

print('aaabbbbccd'.count('b'))
#.count로 문자열에 포함된 문자의 개수를 셀 수 있다

print('abbcccdddd'.find('c'))
print('abbcccdddd'.find('e'))
#find로 처음 해당 문자가 나온 인덱스를 알 수 있다.
#단, 문자열 내에 문자가 포함되어 있지 않은 경우 -1을 반환한다
print('abbcccdddd'.index('d'))
#index는 find와 마찬가지로 처음 해당 문자가 나온 인덱스를 알려주지만 문자열 내에 포함되어 있지
#않은 경우에는 오류가 발생한다.

print(',,,'.join('abcd'))
#대상 문자열 사이에 원하는 문자나 문자열을 집어넣을 수 있다.

print('hi'.upper())
print('HI'.lower())
#소문자로 구성된 문자열을 모두 대문자로 바꿀 수 있다.
#그 반대도 가능하다

a='  hi  '
print(a.lstrip())
print(a.rstrip())
print(a.strip())
#각각 좌,우,양쪽의 공백을 지워 반환한다.

print(a.replace('hi','bye'))
#동일한 문자열을 다른 문자열로 변경한다.

a='Life is too short'
print(a.split())
#split은 공백, 탭, 엔터를 기준으로 문자열을 쪼개 리스트 형태로 반환한다.

b='a,b,c,d'
print(b.split(','))
#쪼개지는 기준을 공백이 아닌 다른 문자로 변경할 수도 있다.