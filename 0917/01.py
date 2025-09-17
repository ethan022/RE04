# break
print('==== break =====')
for i in range(3):
    if i == 2:
        # break를 만나면 for문을 종료 한다.
        break
    print(i)
print()

for i in range(10):
    print(i)
    break

print('for문 종료')
print()

print('==== continue =====')
for i in range(10):
    if i % 2:
        continue
    print(i)
print()

print('==== pass =====')
for i in range(10):
    pass
    print(i)


print('==== for - else =====')
for i in range(10):
    print(i)
    if i == 3:
        break
else:
    print('루프 정상 종료')


print()
colors = ['red', 'blue']
fruits = ['apple', 'banana']

for color in colors:
    for fruit in fruits:
        print(f'{color}, {fruit}')

new_list = [(c, f) for c in colors for f in fruits]

print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
