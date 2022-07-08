def brGame():
    num = 0
    player = 'A'

    def round(num, player):
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
            print(f'player{player} : {num}')
        return num
        
    while num < 31:
        num = round(num, player)
        if player == 'A':
            player = 'B'
        else:
            player = 'A'

    if player == 'A':
        player = 'B'
    else:
        player = 'A'       

    print(f'player{player} win!')
    


brGame()


