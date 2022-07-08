num = 0
player = 'A'

def round():
    ip = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력가능):"))
    try:
        if ip < 1 or ip > 3:
            print("1,2,3만 입력가능")
            round()
        else:
            return ip
    except ValueError:
        print("정수를 입력하세요")
        round()

def record(num):
    for i in range(round()):
        num += 1
        print(f'player{player} : {num}')
    return num

while num < 31:
    num = record(num)
    if player == 'A':
        player = 'B'
    else:
        player = 'A'

