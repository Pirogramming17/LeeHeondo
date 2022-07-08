import random

def brGame():

    num = 0
    player = 'computer'

    def round(num):
        while True:
            try:
                ip = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력가능):"))
                if ip < 1 or ip > 3:
                    print("1,2,3만 입력가능")
                else:
                    break
            except ValueError:
                print("정수를 입력하세요")
                
        for i in range(ip):
            num += 1
            print(f'player: {num}')
        return num

    while num < 31:
        if player == 'computer':
            for i in range(random.randint(1,3)):
                num += 1
                print(f'computer: {num}')
            player = 'player'
        else:
            num = round(num)
            player = 'computer'   

    print(f'{player} win!')
    
brGame()
