# Chapter01-2
# 파이썬 심화
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 클래스 재 선언
class Student():
    """
    Student Class
    Author : Kim
    Date : 2019.05.25
    """

    # 클래스 변수(self(인스턴스들을 나타냄)가 붙는 것들 밖에 존재)
    # 클래스는 항상 속성(def __init__)과 메소드(def detail_info, def __del__)로 이루어져있다.
    # 스코프(영역)가 다름
    student_count = 0

    def __init__(self, name, number, grade, details, email=None): # 생성자를 통해 student1,2,3.....인스턴스를 만드는 것
        # 인스턴스 변수
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email

        Student.student_count += 1 # 클래스의 고유이름(Student)으로 self 밑에 있더라도 클래스 변수에는 접근 가능하다.
                                   # 학생이 한명 생길 때마다 +1씩 되는 것임.

    def __str__(self):
        return 'str {}'.format(self._name)

    def __repr__(self):
        return 'repr {}'.format(self._name)

    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Student Detail Info : {} {} {}'.format(self._name, self._email, self._details))

    def __del__(self):
        Student.student_count -= 1


# Self 의미
studt1 = Student('Cho', 2, 3, {'gender': 'Male', 'score1': 65, 'score2': 44})
studt2 = Student('Chang', 4, 1, {'gender': 'Female', 'score1': 85, 'score2': 74}, 'stu2@naver.com')

# ID 확인
# id는 인스턴스 객체를 만들면 파이썬에서 그거의 고유한 id값을 부여함. id가 달라도 안의 value값은 같을 수 있음.
# 즉 id값이 다르지 않고 같게 생성이 된다면 studt1의 값을 수정하면 studt2의 값도 수정됨.
print(id(studt1))
print(id(studt2))

print(studt1._name == studt2._name) # ==기호는 값(value)가 같다는 의미이지 id가 같다는 의미가 아님
print(studt1 is studt2) # is는 id값이 같은 지 물어보는 것

a = 'ABC'
b = a
print('---------------------------------------')
print('id가 같나요?', a is b)
print('---------------------------------------')

print('---------------------------------------')
print('값이 같나요?', a == b)
print('---------------------------------------')


# dir & __dict__ 확인

print(dir(studt1))
print(dir(studt2))

print()
print()

print(studt1.__dict__)
print(studt2.__dict__)
print()
# Doctring
print('doc', Student.__doc__)
print()
print()
# 실행
studt1.detail_info()
studt2.detail_info()

# 에러
# Student.detail_info() # self라는 객체(인스턴스)가 만들어지기도 전에 바로 접근해버리니 없는 걸 불러오는 꼴이 되면서 에러가 난다.

Student.detail_info(studt1)
Student.detail_info(studt2)

# 비교
print(studt1.__class__, studt2.__class__)
print(id(studt1.__class__) == id(studt2.__class__))

print()

# 인스턴스 변수
# 직접 접근(PEP 문법적으로 권장X)

print(studt1._name, studt2._name)
print(studt1._email, studt2._email)

print()
print()

# 클래스 변수

# 접근
print(studt1.student_count)
print(studt2.student_count)
print(Student.student_count)

print()
print()


# 공유 확인
print(Student.__dict__)
print(studt1.__dict__)
print(studt2.__dict__)

# 인스턴스 네임스페이스 없으면 상위에서 검색
# 즉, 인스턴스 검색 후 없다면? -> 상위(클래스 변수, 부모 클래스 변수)쪽을 검색함. 파이썬이라는 프로그램 자체가 그래용...

del studt2

print(studt1.student_count)
print(Student.student_count)