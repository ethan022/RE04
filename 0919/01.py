#  함수의 범위(Scope)

'''
    변수의 범위란?
    변수가 살아있는(접근 가능한)영역을 범위(Scope)라고 합니다.
    비유:
    집 = 전역범위
    방 = 지역범위
    방 안의 물건은 그 방에서만 사용 가능
    거실의 물건은 모든 방에서 사용 가능
'''


# 전역 변수(Global Variable)
global_var = '전역 변수'


def my_fun():
    # 지역 변수 (Local Variable)
    local_var = '지역 변수'

    print(global_var)  # 전역 변수 접근 가능
    print(local_var)  # 지역 변수 접근 가능


my_fun()
print(global_var)  # 전역 변수 접근 가능
# print(local_var)  # 에러! 함수 밖에서 지역 변수 접근 불가


# Global 키워드
# 함수 안에서 전역 변수를 수정하려면 global 키워드를 사용합니다.

count = 0  # 전역 변수


# def increment_wrong():
#     count += 1  # 에러! 지역 변수로 취급됨


def increment_right():
    global count
    count = count + 1


# increment_wrong()

print('초기값:', count)  # 0
increment_right()
increment_right()
print('최종값:', count)  # 2


score = 0


def add_score(points):
    global score
    score += points
    print(f'점수 획득! 현재 점수: {score}')


def reset_score():
    global score
    score = 0
    print('점수 초기화!!')


add_score(100)
add_score(200)

print(score)  # 300

reset_score()

print(score)  # 0


# 전역 변수 사용 주의
# 전역 변수는 편리하지만 과도하게 사용하면 코드가 복잡해집니다.

total = 0
count = 0


def add_number(num):
    global total, count
    total += num
    count += 1


def get_average():
    global total, count  # 남용 예시
    return total / count if count > 0 else 0


# 좋은 예
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


numbers = [53, 56, 34, 64,]
avg = calculate_average(numbers=numbers)


# ====================================

# 복사본이 넘어옴
def increment_num(num_copy):
    num_copy += 1


# 함수에 원본 그대로 넘어옴
def num_append(numbers):
    numbers.append(6)
    numbers[0] += 1
    # number += 1


# 불변 타입
# 정수, 실수, 문자열, 튜플
num = 10
print('함수 호출 전, num:', num)  # 10
increment_num(num_copy=num)
print('함수 호출 후, num:', num)  # 10

# 가변타입
# 리스트, 딕셔너리, set
numbers = [1, 2, 3, 4, 5]
print('함수 호출 전, numbers:', numbers)  # 1
num_append(numbers=numbers)
print('함수 호출 후, numbers', numbers)  # 2


info_dic = {'name': '김철수', 'age': 20}


def change_info(info):
    info['name'] = '이영희'
    info['age'] = 25


# 1 {'name': '김철수', 'age': 20}
print('함수 호출 전, info_dic:', info_dic)
change_info(info_dic)
# 2 {'name': '이영희', 'age': 25}
print('함수 호출 후, info_dic', info_dic)


# 재귀 함수 (Recursive Function)
'''
    재귀 함수는 자기 자신을 호출하는 함수
'''


def recursive_function(n):
    # 1. 기저 조건(Base Case)
    if n == 종료_조건:
        return 기저값

    # 2. 재귀 호출(Recursive Call)
    return recursive_function(n을_작게_만든_값)


# 팩토리얼 계산 (n! = n x (n-1) x (n-2) x (n-3) .... 1)


def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n-1)


result = factorial(5)  # 5 x 4 x 3 x 2 x 1 = 120
print(result)
# 5 x factorial(4)
# 5 x 4 x factorial(3)
# 5 x 4 x 3 x factorial(2)
# 5 x 4 x 3 x 2 x 1


# 피보나치 수열
# 0 1 1 2 3 5 8 13 ....

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n-2) + fibonacci(n-1)


fibonacci(2)
# fibonacci(1) + fibonacci(0)
# 1 + 0
# 1
fibonacci(4)
# fibonacci(2) + fibonacci(3)
# fibonacci(0) + fibonacci(1) + fibonacci(3)
# 0 +  1 + fibonacci(3)
# 0 +  1 + fibonacci(1) + fibonacci(2)
# 0 +  1 + 1 + 0 + 1
# 3

#
#

# for i in range(10):
#     print(fibonacci(i))
# print()


# def recursive_function(n):
#     # 1. 기저 조건(Base Case)
#     if n == 종료_조건:
#         return 기저값

#     # 2. 재귀 호출(Recursive Call)
#     return recursive_function(n을_작게_만든_값)


# 람다 함수(lambda Function)
'''
    람다 함수는 이름 없는 한 줄까지 간단한 함수 입니다.
'''

# 일반 함수
def sqare(x):
    return x ** 2

# 람다 함수 (같은 기능)
square_lambda = lambda x: x ** 2


print('sqare(5)', sqare(5))
print('square_lambda(5)', square_lambda(5))


# 여러 매개변수
add = lambda x, y: x+ y
print(add(5,3))

# map(): 모든 요소에 함수 적용
numbers = [1,2,3,4,5]

squared= list(map(lambda x: x ** 2, numbers))
# [1, 4, 9, 16, 25]

def increment_fun(x):
    return x + 1

incre_numbers = list(map(increment_fun, numbers))
print(incre_numbers)

# filter
evens = list(filter(lambda x: x > 3, numbers))
print(evens)

# sorted() 정렬 기준 지정

students = [
     {'name': "홍길동", 'score': 80},
     {'name': "김철수", 'score': 92},
     {'name': "이영희", 'score': 72}
]

students.sort(key=lambda x: x['name'])
for student in students:
    print(f'{student['name']}: {student['score']}점')