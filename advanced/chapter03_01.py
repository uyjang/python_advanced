# Chapter03-1
# 파이썬 심화
# 시퀀스형 
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque], Flat : 한 개의 자료형[str,bytes,bytearray,array.array, memoryview]) # 한개의 자료형을 저장하는 게 속도는 훨씬 빠름.
# 가변(list, bytearray, array.array, memoryview, deque) vs 불변(tuple, str, bytes)
# 리스트 및 튜플 심화

# 지능형 리스트(Comprehending Lists) # 리스트는 100만개를 생성했으면 바로 메모리에 실어서 메모리에 공간차지를 하게 함. 그러나 제네레이터는 만들어놓고 메모리에 적재는 안해놓음.

# Non Comprehending Lists
chars = '!@#$%^&*()_+'
codes1 = []

for s in chars:
    # 유니코드 리스트
    codes1.append(ord(s)) # ord는 문자(특수문자)를 숫자로 출력해주는 것

# Comprehending Lists
codes2 = [ord(s) for s in chars]

# Comprehending Lists + Map, Filter
# 속도 약간 우세
codes3 = [ord(s) for s in chars if ord(s) > 40]
codes4 = list(filter(lambda x : x > 40, map(ord, chars))) # ord(문자->숫자)로 만들것이야 무엇을? chars에 있는 데이터를

# 전체 출력
print('EX1-1 -', codes1)
print('EX1-2 -', codes2)
print('EX1-3 -', codes3)
print('EX1-4 -', codes4)
print('EX1-5 -', [chr(s) for s in codes1])
print('EX1-6 -', [chr(s) for s in codes2])
print('EX1-7 -', [chr(s) for s in codes3])
print('EX1-8 -', [chr(s) for s in codes4])

print()
print()


# Generator 생성 방법

import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지X) # 그때 그때 하나씩만 대응해주면 되는 프로그램에서는 제네레이터가 나음.
tuple_g = (ord(s) for s in chars) # 괄호(튜플형태)로 리스트 컴프리헨션 양식을 해주면 제네레이터가 생성이 됨.
# Array
array_g = array.array('I',  (ord(s) for s in chars)) # 단일타입의 데이터를 저장할 때 사용

print('EX2-1 -', type(tuple_g))
print('EX2-2 -', next(tuple_g)) # 이걸 써야 데이터가 나오는데 한개만 나옴. 한번에 한개만 생성한다고 했으니까....
print('EX2-3 -', array_g)
print('EX2-4 -', array_g.tolist())

print()
print()

# 제네레이터 예제
print('EX3-1 -', ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)):
    print('EX3-2 -', s)


print()
print()

# 리스트 주의 할 점
marks1 = [['~'] * 3 for n in range(3)] # 리스트 컴프리헨션은 id가 다른 객체(여기서는 리스트)를 만들어준다.
marks2 = [['~'] * 3] * 3               # 그러나 그냥 곱하기3을 해버리면 똑같은 id를 가진 객체(여기서는 리스트)를 그냥 세번 똑같이 복사붙여넣기하는 것이다.

print('EX4-1 -', marks1)
print('EX4-2 -', marks2)

print()

# 수정
marks1[0][1] = 'X'
marks2[0][1] = 'X'

print('EX4-3 -', marks1)
print('EX4-4 -', marks2)

# 증명
print('EX4-5 -', [id(i) for i in marks1])
print('EX4-6 -', [id(i) for i in marks2])

# Tuple Advanced

# Unpacking

# b, a = a, b

print('EX5-1 -', divmod(100, 9))
print('EX5-2 -', divmod(*(100, 9))) # 여기서 *표는 안에서 알아서 풀어서 사용해라 라는 느낌. 즉 유동성을 주는 것
print('EX5-3 -', *(divmod(100, 9)))

print()

x, y, *rest = range(10)
print('EX5-4 -', x, y, rest)
x, y, *rest = range(2) # 여기서 *표는 데이터가 몇개 들어올 지 모르니 리스트형태로 만들어 놓음. 어쨋든 이것도 유동성을 줌.
                       # 즉 *표가 인자로 들어왔을 때는 알아서 언패킹해라 라는 뜻이고 *표가 변수에 들어가 있을 때는 리스트형태로 묶어서 보여줌.
print('EX5-5 -', x, y, rest)
x, y, *rest = 1, 2, 3, 4, 5
print('EX5-6 -', x, y, rest)

print()
print()

# Mutable(가변) vs Immutable(불변)

l = (10, 15, 20)
m = [10, 15, 20]

print('EX6-1 -', l, id(l))
print('EX6-2 -', m, id(m))

l = l * 2
m = m * 2 # 리스트의 경우 연산을 수행 할 때 이러한 방식으로 재할당을 해줘야 새로운 id를 만들어서 새 객체를 만듦.

print('EX6-3 -', l, id(l))
print('EX6-4 -', m, id(m))

l *= 2
m *= 2

# 튜플은 위의 두가지 방식을 써도 새로운 id를 만들어서 새 객체를 만들어 사용.

print('EX6-5 -', l, id(l))
print('EX6-6 -', m, id(m))

print()
print()

# sort vs sorted 
# reverse, key=len, key=str.lower, key=func..

# sorted : 정렬 후 새로운 객체 반환
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']

print('EX7-1 -', sorted(f_list))
print('EX7-2 -', sorted(f_list, reverse=True))
print('EX7-3 -', sorted(f_list, key=len))
print('EX7-4 -', sorted(f_list, key=lambda x: x[-1]))
print('EX7-5 -', sorted(f_list, key=lambda x: x[-1], reverse=True))
print()

print('EX7-6 -', f_list)

print()

# sort : 정렬 후 객체 직접 변경(새로운 객체를 만들지 않고 원본이 바뀜)

# 반환 값 확인(None)
print('EX7-7 -', f_list.sort(), f_list)
print('EX7-8 -', f_list.sort(reverse=True), f_list)
print('EX7-9 -', f_list.sort(key=len), f_list)
print('EX7-10 -', f_list.sort(key=lambda x: x[-1]), f_list)
print('EX7-11 -', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)

# List vs Array 적합 한 사용법 설명
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반 : 배열(리스트의 거의 모든 연산 지원)