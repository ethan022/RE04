# 파이썬 내장함수 및 random 모듈 완전 가이드

"""
이 가이드는 파이썬에서 자주 사용되는 내장함수들과 random 모듈의 
다양한 함수들을 실전 예제와 함께 설명합니다.

주요 내용:
1. random 모듈 - 난수 생성과 무작위 선택
2. 수학 관련 내장함수 - abs, round, min, max, sum 등
3. 문자열/리스트 관련 내장함수 - len, sorted, reversed 등
4. 타입 변환 함수 - int, float, str, list, tuple 등
5. 입출력 함수 - input, print의 고급 활용
6. 기타 유용한 함수들 - zip, enumerate, range 등
"""

from collections import Counter
import random
import math

print("=" * 80)
print("🎲 RANDOM 모듈 - 난수 생성과 무작위 선택")
print("=" * 80)

# ================================
# 1. random 모듈 기본 함수들
# ================================

print("\n[ 1. random.random() - 0.0 이상 1.0 미만의 실수 ]")
print("기본 난수 생성기, 가장 기본적인 함수")

for i in range(5):
    rand_float = random.random()
    print(f"  시도 {i+1}: {rand_float:.6f}")

print("\n활용 예제: 확률 기반 이벤트")


def probability_event(success_rate):
    """주어진 확률로 성공/실패를 결정"""
    return random.random() < success_rate


# 30% 확률로 성공하는 이벤트 10번 시뮬레이션
successes = 0
for i in range(10):
    if probability_event(0.3):  # 30% 확률
        successes += 1
        print(f"  시도 {i+1}: ✅ 성공!")
    else:
        print(f"  시도 {i+1}: ❌ 실패")

print(f"  총 성공률: {successes}/10 = {successes*10}%")

print("\n" + "-" * 60)
print("[ 2. random.randint(a, b) - a 이상 b 이하의 정수 ]")
print("양 끝값을 포함하는 정수 난수 생성")

print("주사위 굴리기 (1~6):")
dice_results = []
for i in range(10):
    dice = random.randint(1, 6)
    dice_results.append(dice)
    print(f"  굴리기 {i+1}: {dice}")

print(f"결과 분석: 평균 = {sum(dice_results)/len(dice_results):.2f}")

print("\n로또 번호 생성기 (1~45 중 6개, 중복 없음):")
lotto_numbers = []
while len(lotto_numbers) < 6:
    number = random.randint(1, 45)
    if number not in lotto_numbers:  # 중복 방지
        lotto_numbers.append(number)

lotto_numbers.sort()  # 정렬해서 보기 좋게
print(f"  🎰 로또 번호: {lotto_numbers}")

print("\n" + "-" * 60)
print("[ 3. random.choice(sequence) - 시퀀스에서 하나의 요소 선택 ]")
print("리스트, 튜플, 문자열 등에서 무작위로 하나 선택")

# 기본 사용법
colors = ['빨강', '파랑', '노랑', '초록', '보라']
foods = ('피자', '햄버거', '치킨', '파스타', '스시')
greeting = "안녕하세요"

print("무작위 선택 예제:")
for i in range(5):
    chosen_color = random.choice(colors)
    chosen_food = random.choice(foods)
    chosen_char = random.choice(greeting)
    print(f"  {i+1}: {chosen_color} 색의 {chosen_food}, 문자 '{chosen_char}'")

print("\n실전 활용: 랜덤 문장 생성기")
subjects = ['고양이가', '강아지가', '새가', '토끼가', '코끼리가']
actions = ['뛰어다니고', '잠을 자고', '밥을 먹고', '노래하고', '춤추고']
objects = ['공원에서 놀았다', '집에서 쉬었다', '친구를 만났다', '모험을 떠났다']

print("🎭 랜덤 동화 생성:")
for i in range(3):
    sentence = f"{random.choice(subjects)} {random.choice(actions)} {random.choice(objects)}"
    print(f"  이야기 {i+1}: {sentence}")

print("\n" + "-" * 60)
print("[ 4. random.choices(sequence, k=n) - 중복 허용하여 n개 선택 ]")
print("동일한 요소가 여러 번 선택될 수 있음")

menu = ['떡볶이', '순대', '튀김', '김밥', '라면']

print("분식점 주문 시뮬레이션 (중복 주문 가능):")
# 5번 주문 (같은 메뉴 여러 번 주문 가능)
orders = random.choices(menu, k=5)
print(f"  주문 내역: {orders}")

# 주문 통계
order_count = Counter(orders)
print("  주문 통계:")
for item, count in order_count.items():
    print(f"    {item}: {count}개")

print("\n가중치가 있는 선택 (weights 매개변수):")
# 각 메뉴별로 선택될 확률을 다르게 설정
weights = [30, 20, 25, 15, 10]  # 떡볶이가 가장 인기
weighted_orders = random.choices(menu, weights=weights, k=10)
print(f"  가중치 적용 주문: {weighted_orders}")

weighted_count = Counter(weighted_orders)
print("  가중치 적용 통계:")
for item, count in weighted_count.items():
    percentage = (count / 10) * 100
    print(f"    {item}: {count}개 ({percentage}%)")

print("\n" + "-" * 60)
print("[ 5. random.sample(sequence, k) - 중복 없이 k개 선택 ]")
print("동일한 요소는 한 번만 선택됨")

participants = ['김철수', '이영희', '박민수', '최지연', '정다영',
                '윤서준', '한소미', '조현우', '신예린', '오태현']

print("🏆 경품 추첨 (중복 당첨 없음):")
winners = random.sample(participants, k=3)
prizes = ['1등: 아이폰', '2등: 에어팟', '3등: 스타벅스 기프티콘']

for i, winner in enumerate(winners):
    print(f"  {prizes[i]} - {winner}")

print(f"\n당첨자 외 참가자: {[p for p in participants if p not in winners]}")

print("\n팀 나누기:")
team_size = 4
teams = []
remaining = participants.copy()

team_num = 1
while len(remaining) >= team_size:
    team = random.sample(remaining, k=team_size)
    teams.append(team)
    print(f"  팀 {team_num}: {team}")

    # 선택된 사람들을 remaining에서 제거
    for member in team:
        remaining.remove(member)
    team_num += 1

if remaining:
    print(f"  남은 인원: {remaining}")

print("\n" + "-" * 60)
print("[ 6. random.shuffle(sequence) - 리스트를 무작위로 섞기 ]")
print("원본 리스트를 직접 수정 (in-place 연산)")

# 카드 덱 만들기
suits = ['♠', '♥', '♦', '♣']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = [f"{suit}{rank}" for suit in suits for rank in ranks]

print(f"카드 덱 생성 완료: 총 {len(deck)}장")
print(f"셔플 전 처음 10장: {deck[:10]}")

# 카드 섞기
random.shuffle(deck)
print(f"셔플 후 처음 10장: {deck[:10]}")

# 카드 나누기
print("\n🃏 포커 게임: 각자 5장씩 배분")
players = ['플레이어1', '플레이어2', '플레이어3', '플레이어4']
hands = {player: [] for player in players}

for _ in range(5):  # 5장씩 나누어주기
    for player in players:
        card = deck.pop()  # 덱에서 카드 한 장 빼기
        hands[player].append(card)

for player, cards in hands.items():
    print(f"  {player}: {cards}")

print("\n" + "-" * 60)
print("[ 7. random.uniform(a, b) - a와 b 사이의 실수 ]")
print("특정 범위의 실수 난수 생성")

print("온도 시뮬레이션 (18.5°C ~ 25.3°C):")
for day in range(7):
    temperature = random.uniform(18.5, 25.3)
    print(f"  {day+1}일차: {temperature:.1f}°C")

print("\n키와 몸무게 랜덤 생성:")
for i in range(5):
    height = random.uniform(150, 190)  # 키 (cm)
    weight = random.uniform(45, 85)    # 몸무게 (kg)
    bmi = weight / ((height/100) ** 2)
    print(f"  사람 {i+1}: {height:.1f}cm, {weight:.1f}kg (BMI: {bmi:.1f})")

print("\n" + "=" * 80)
print("🔢 수학 관련 내장함수")
print("=" * 80)

# ================================
# 2. 수학 관련 내장함수
# ================================

print("\n[ abs() - 절댓값 ]")
print("음수를 양수로, 양수는 그대로")

numbers = [-10, -3.14, 0, 5, 15.7]
print("절댓값 계산:")
for num in numbers:
    print(f"  abs({num}) = {abs(num)}")

print("\n실전 활용: 두 점 사이의 거리")


def distance_1d(x1, x2):
    """1차원에서 두 점 사이의 거리"""
    return abs(x2 - x1)


point_pairs = [(10, 3), (-5, 7), (0, -8)]
for x1, x2 in point_pairs:
    dist = distance_1d(x1, x2)
    print(f"  점 {x1}과 점 {x2} 사이의 거리: {dist}")

print("\n" + "-" * 60)
print("[ round() - 반올림 ]")
print("소수점 자리수 지정 가능")

values = [3.14159, 2.71828, 1.41421, 9.99999, 10.5, 11.5]

print("다양한 반올림:")
for val in values:
    print(f"  {val} → 정수: {round(val)}, 소수점 2자리: {round(val, 2)}")

print("\n성적 평균 계산:")
scores = [85.7, 92.3, 78.9, 88.1, 95.6]
average = sum(scores) / len(scores)
print(f"  원점수들: {scores}")
print(f"  평균: {average} → 반올림: {round(average, 1)}")

print("\n" + "-" * 60)
print("[ min(), max() - 최솟값, 최댓값 ]")
print("여러 값 또는 시퀀스에서 최솟값/최댓값 찾기")

# 여러 값에서 찾기
temp_today = [15.2, 18.7, 22.1, 19.8, 16.3]
print(f"오늘 온도 변화: {temp_today}")
print(f"  최저온도: {min(temp_today)}°C")
print(f"  최고온도: {max(temp_today)}°C")
print(f"  온도차: {max(temp_today) - min(temp_today):.1f}°C")

# 여러 인수로 사용
print(f"\nmin(10, 5, 15, 3) = {min(10, 5, 15, 3)}")
print(f"max(10, 5, 15, 3) = {max(10, 5, 15, 3)}")

# 문자열에서도 사용 가능 (사전순)
names = ['김철수', '이영희', '박민수', '최지연']
print(f"\n이름 리스트: {names}")
print(f"  사전순 첫 번째: {min(names)}")
print(f"  사전순 마지막: {max(names)}")

print("\n성적 분석:")
student_scores = {
    '김철수': 85,
    '이영희': 92,
    '박민수': 78,
    '최지연': 88,
    '정다영': 95
}

# 점수만 추출해서 최고/최저 찾기
scores = student_scores.values()
min_score = min(scores)
max_score = max(scores)

# 최고/최저 점수 받은 학생 찾기
top_student = max(student_scores, key=student_scores.get)
bottom_student = min(student_scores, key=student_scores.get)

print(f"  최고점: {max_score}점 ({top_student})")
print(f"  최저점: {min_score}점 ({bottom_student})")

print("\n" + "-" * 60)
print("[ sum() - 합계 ]")
print("숫자 시퀀스의 총합 계산")

# 기본 사용법
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(f"{numbers}의 합: {total}")

# 시작값 지정
total_with_start = sum(numbers, 100)  # 100부터 시작해서 더함
print(f"{numbers}의 합 (시작값 100): {total_with_start}")

# 실전 활용: 쇼핑몰 장바구니
cart_items = {
    '노트북': 1200000,
    '마우스': 50000,
    '키보드': 120000,
    '모니터': 300000
}

print("\n🛒 쇼핑몰 장바구니:")
for item, price in cart_items.items():
    print(f"  {item}: {price:,}원")

total_price = sum(cart_items.values())
print(f"  총 금액: {total_price:,}원")

# 할인 적용
if total_price >= 1000000:
    discount = total_price * 0.1  # 10% 할인
    final_price = total_price - discount
    print(f"  할인액 (10%): -{discount:,}원")
    print(f"  최종 금액: {final_price:,}원")

print("\n" + "=" * 80)
print("📝 문자열/리스트 관련 내장함수")
print("=" * 80)

# ================================
# 3. 문자열/리스트 관련 내장함수
# ================================

print("\n[ len() - 길이 ]")
print("문자열, 리스트, 튜플, 딕셔너리 등의 길이")

examples = [
    "안녕하세요",
    [1, 2, 3, 4, 5],
    (10, 20, 30),
    {'a': 1, 'b': 2, 'c': 3},
    {1, 2, 3, 4}
]

print("다양한 객체의 길이:")
for i, obj in enumerate(examples, 1):
    print(f"  {i}. {obj} → 길이: {len(obj)}")

print("\n비밀번호 강도 검사:")


def check_password_strength(password):
    """비밀번호 강도를 검사하는 함수"""
    length = len(password)
    if length < 6:
        return "약함 (6자 미만)"
    elif length < 10:
        return "보통 (6-9자)"
    else:
        return "강함 (10자 이상)"


test_passwords = ['123', 'password', 'mypassword123']
for pwd in test_passwords:
    strength = check_password_strength(pwd)
    print(f"  '{pwd}' ({len(pwd)}자): {strength}")

print("\n" + "-" * 60)
print("[ sorted() - 정렬 ]")
print("원본을 변경하지 않고 새로운 정렬된 리스트 반환")

# 기본 정렬
numbers = [64, 34, 25, 12, 22, 11, 90]
names = ['김철수', '이영희', '박민수', '최지연']

print("숫자 정렬:")
print(f"  원본: {numbers}")
print(f"  오름차순: {sorted(numbers)}")
print(f"  내림차순: {sorted(numbers, reverse=True)}")
print(f"  원본 확인: {numbers}")  # 원본은 변경되지 않음

print("\n한글 이름 정렬:")
print(f"  원본: {names}")
print(f"  가나다순: {sorted(names)}")
print(f"  역순: {sorted(names, reverse=True)}")

# key 매개변수 활용
print("\n고급 정렬 - key 매개변수:")
words = ['python', 'java', 'c', 'javascript', 'go']

print(f"원본: {words}")
print(f"길이순 정렬: {sorted(words, key=len)}")
print(f"길이 역순: {sorted(words, key=len, reverse=True)}")

# 학생 성적 정렬
students = [
    ('김철수', 85, 'A'),
    ('이영희', 92, 'A+'),
    ('박민수', 78, 'B'),
    ('최지연', 88, 'A'),
    ('정다영', 95, 'A+')
]

print("\n학생 성적 정렬:")
print("점수순 (오름차순):")
by_score = sorted(students, key=lambda x: x[1])
for name, score, grade in by_score:
    print(f"  {name}: {score}점 ({grade})")

print("\n점수순 (내림차순):")
by_score_desc = sorted(students, key=lambda x: x[1], reverse=True)
for name, score, grade in by_score_desc:
    print(f"  {name}: {score}점 ({grade})")

print("\n" + "-" * 60)
print("[ reversed() - 역순 ]")
print("시퀀스의 요소들을 역순으로 반환 (iterator 객체)")

original_list = [1, 2, 3, 4, 5]
original_string = "Hello"

print(f"리스트 역순: {original_list} → {list(reversed(original_list))}")
print(f"문자열 역순: '{original_string}' → '{''.join(reversed(original_string))}'")

# 실전 활용: 회문(palindrome) 검사


def is_palindrome(text):
    """회문인지 검사하는 함수"""
    # 공백과 대소문자 무시
    clean_text = text.replace(' ', '').lower()
    return clean_text == ''.join(reversed(clean_text))


test_words = ['level', 'hello', 'A man a plan a canal Panama', '기러기', '파이썬']
print("\n회문 검사:")
for word in test_words:
    result = is_palindrome(word)
    print(f"  '{word}': {'✅ 회문' if result else '❌ 회문 아님'}")

print("\n" + "=" * 80)
print("🔄 타입 변환 내장함수")
print("=" * 80)

# ================================
# 4. 타입 변환 함수
# ================================

print("\n[ int(), float(), str() - 기본 타입 변환 ]")

# 다양한 변환 예제
conversion_examples = [
    ("문자열 → 정수", "123", int),
    ("실수 → 정수", 3.14, int),
    ("정수 → 실수", 42, float),
    ("문자열 → 실수", "3.14", float),
    ("정수 → 문자열", 123, str),
    ("실수 → 문자열", 3.14, str)
]

print("타입 변환 예제:")
for description, value, func in conversion_examples:
    try:
        result = func(value)
        print(f"  {description}: {value} → {result} (타입: {type(result).__name__})")
    except ValueError as e:
        print(f"  {description}: {value} → 변환 실패 ({e})")

# 진법 변환
print("\n진법 변환:")
number = 42
print(f"10진수 {number}:")
print(f"  2진수: {bin(number)}")
print(f"  8진수: {oct(number)}")
print(f"  16진수: {hex(number)}")

# 역변환
binary_str = "101010"
print(f"\n2진수 '{binary_str}' → 10진수: {int(binary_str, 2)}")

print("\n" + "-" * 60)
print("[ list(), tuple(), set(), dict() - 컬렉션 변환 ]")

# 원본 데이터
original_string = "python"
original_list = [1, 2, 3, 2, 1]
original_tuple = (10, 20, 30)

print("컬렉션 간 변환:")
print(f"문자열 → 리스트: '{original_string}' → {list(original_string)}")
print(f"리스트 → 튜플: {original_list} → {tuple(original_list)}")
print(f"리스트 → 집합: {original_list} → {set(original_list)}")  # 중복 제거됨
print(f"튜플 → 리스트: {original_tuple} → {list(original_tuple)}")

# 딕셔너리 생성
key_value_pairs = [('이름', '김철수'), ('나이', 25), ('직업', '개발자')]
person_dict = dict(key_value_pairs)
print(f"리스트 → 딕셔너리: {key_value_pairs}")
print(f"                → {person_dict}")

# 실전 활용: 중복 제거
print("\n실전 활용 - 중복 제거:")
duplicated_list = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique_list = list(set(duplicated_list))  # 집합으로 변환 후 다시 리스트로
print(f"  원본: {duplicated_list}")
print(f"  중복제거: {unique_list}")
print(f"  순서유지 중복제거: {list(dict.fromkeys(duplicated_list))}")

print("\n" + "=" * 80)
print("📥📤 입출력 함수")
print("=" * 80)

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
