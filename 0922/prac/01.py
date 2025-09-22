class Book:
    def __init__(self, title, author, total_pages):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = 0

    def read_page(self, pages):
        '''현재 페이지를 읽음. 총 페이지 수를 넘지 않도록 처리.'''
        if pages < 0:
            return

        self.current_page = min(self.total_pages, self.current_page + pages)

    def progress(self):
        '''
        전체에서 얼마나 읽었는지를 퍼센트( % )로 소수점 1자리까지 출력
        '''
        pct = (self.current_page / self.total_pages) * 100
        return round(pct, 1)

    def __repr__(self):
        return f"< Book {self.title} by {self.author} >"


# 객체 생성
b = Book('파이썬 클린코드', '홍길동', total_pages=320)
b.read_page(100)
print()
print('책 정보')
print(b)
print()
print(b.progress(), '%')
print()
b.read_page(1000)
print()
print(b.progress(), '%')
print()


class Rectangle:
    # 생성자!!!!
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        ''' 사각형의 넓이 반환'''
        return self.width * self.height


w = int(input('너비를 입력해주세요:'))
h = int(input('높이를 입력해주세요:'))

rect = Rectangle(w, h)
print('사각형의 넓이: ', rect.area())


class User:
    total_users = 0

    def __init__(self, name):
        self.username = name
        self.points = 0
        # 클래스 변수 업데이트
        User.total_users += 1

    def add_points(self, amount):
        '''포인트 추가'''
        self.points += amount

    def get_level(self):
        '''포인트 기준으로 레벨 반환'''
        if 0 <= self.points < 100:
            return 'Bronze'
        elif 100 <= self.points < 500:
            return 'Silver'
        elif 500 <= self.points:
            return 'Gold'

    @classmethod
    def get_total_users(cls):
        print(f'총 유저 수 : {cls.total_users}')

    def __del__(self):
        User.total_users -= 1


user1 = User('김철수')
user2 = User('홍길동')
user3 = User('이영희')

User.get_total_users()  # 3

del user2

User.get_total_users()  # 2
