
# ================================
# 5. 입출력 함수
# ================================

print("\n[ print() - 출력 함수의 고급 활용 ]")

# 기본 구분자 변경
print("구분자 변경:")
print("  기본:", 1, 2, 3, 4, 5)
print("  쉼표로:", 1, 2, 3, 4, 5, sep=', ')
print("  대시로:", 1, 2, 3, 4, 5, sep=' - ')
print("  구분자 없이:", 1, 2, 3, 4, 5, sep='')

# 끝 문자 변경
print("\n끝 문자 변경:")
print("첫 번째 줄", end=' ')
print("같은 줄 계속")
print("새 줄에서", end='!!!\n')
print("다음 줄")

# 다양한 출력 방법
print("\n다양한 출력 형식:")
name = "김철수"
age = 25
score = 85.67

print(f"f-string: {name}님은 {age}세이고 점수는 {score:.1f}점입니다.")
print("format: {}님은 {}세이고 점수는 {:.1f}점입니다.".format(name, age, score))
print("% 포매팅: %s님은 %d세이고 점수는 %.1f점입니다." % (name, age, score))

print("\n표 형태 출력:")
students_data = [
    ('김철수', 25, 85.67),
    ('이영희', 24, 92.45),
    ('박민수', 26, 78.23)
]

print(f"{'이름':<10} {'나이':<5} {'점수':<8}")
print("-" * 25)
for name, age, score in students_data:
    print(f"{name:<10} {age:<5} {score:<8.2f}")

# input() 시뮬레이션 (실제로는 사용자 입력)
print("\n[ input() - 입력 함수 시뮬레이션 ]")
print("실제 사용 예제들:")

# 타입 변환과 함께 사용하는 패턴들
input_examples = """
# 정수 입력받기
age = int(input('나이를 입력하세요: '))

# 실수 입력받기  
height = float(input('키를 입력하세요(cm): '))

# 여러 값을 한 번에 입력받기
numbers = input('숫자들을 공백으로 구분해서 입력: ').split()
numbers = [int(x) for x in numbers]

# 예/아니오 입력받기
answer = input('계속하시겠습니까? (y/n): ').lower().strip()
continue_flag = answer in ['y', 'yes', '예', 'ㅇ']
"""
print(input_examples)

print("\n" + "=" * 80)
print("🔧 기타 유용한 내장함수")
print("=" * 80)
