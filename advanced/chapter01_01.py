# Chapter01-1
# 파이썬 심화
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 일반적인 코딩

# 학생1
student_name_1 = 'Kim'
student_number_1 = 1
student_grade_1 = 1
student_detail_1 = [
    {'gender' : 'Male'},
    {'score1': 95},
    {'score2': 88}
]

# 학생2
student_name_2 = 'Lee'
student_number_2 = 2
student_grade_2 = 2
student_detail_2 = [
    {'gender' : 'Female'},
    {'score1': 77},
    {'score2': 92}
]

# 학생3
student_name_3 = 'Park'
student_number_3 = 3
student_grade_3 = 4
student_detail_3 = [
    {'gender' : 'Male'},
    {'score1': 99},
    {'score2': 100}
]


# 리스트 구조
# 관리하기 불편
# 데이터의 정확한 위치(인덱스)매핑 해서 사용
student_names_list = ['Kim', 'Lee', 'Park']
student_numbers_list = [1, 2, 3]
student_grades_list = [1, 2, 4]
student_details_list = [
    {'gender' : 'Male', 'score1': 95, 'score2': 88},
    {'gender' : 'Female', 'score1': 77, 'score2': 92},
    {'gender' : 'Male', 'score1': 99, 'score2': 100}
]

# 학생 삭제
del student_names_list[1]
del student_numbers_list[1]
del student_grades_list[1]
del student_details_list[1]

print('--------------------1-----------------------------------')
print(student_names_list)
print(student_numbers_list)
print(student_grades_list)
print(student_details_list)

print()
print()


# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제
# 외부에 있는 데이터베이스나 문서로부터 데이터를 끌어오는 데 그 외부에 있는 것들을 써드파티라고 하고 써드파티는 주로 딕트형태(제이슨형태)로 가지고 옴
students_dicts = [
    {'student_name': 'Kim', 'student_number': 1, 'student_grade': 1, 'student_detail': {'gender': 'Male', 'score1': 95, 'score2': 88}},
    {'student_name': 'Lee', 'student_number': 2, 'student_grade': 2, 'student_detail': {'gender': 'Female', 'score1': 77, 'score2': 92}},
    {'student_name': 'Park', 'student_number': 3, 'student_grade': 4, 'student_detail': {'gender': 'Male', 'score1': 99, 'score2': 100}}
]

del students_dicts[1]
print('-----------------------------2---------------------------------')
print(students_dicts)
print()
print()


# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

class Student():
    def __init__(self, name, number, grade, details): # 생성자, constructor
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details

    def __str__(self): # 이걸 설정안하면 나중에 인스턴스 만들었을 때(ex.student1)의 값을 부르면 0x0000023579~이렇게 나옴. 근데 설정을 하면 내가 설정한 대로 보여줌. 오버라이드 한것임 ㅎ
        return 'str : {} - {}'.format(self._name, self._number)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._name, self._number)
    

student1 = Student('Kim', 1, 1, {'gender': 'Male', 'score1': 95, 'score2': 88})
student2 = Student('Lee', 2, 2, {'gender': 'Female', 'score1': 77, 'score2': 92})
student3 = Student('Park', 3, 4, {'gender': 'Male', 'score1': 99, 'score2': 100})

print(student1.__dict__) # 우리가 생성한 student1이라는 것에 여러 속성값들이 들어있고 그 속성값들은 네임스페이스라는 곳에 저장되도록 파이썬은 설계돼있음.
print(student2.__dict__)
print(student3.__dict__)

# 리스트 선언
students_list = []

students_list.append(student1)
students_list.append(student2)
students_list.append(student3)

print()

print(students_list)

print()
print()

# 반복(__str__)
for x in students_list:
    print(repr(x))
    print(x)