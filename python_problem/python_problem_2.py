num = 0
ip = int(input("부를 숫자의 개수를 입력하세요(1,2,3만 입력가능):"))

while True:
    if type(ip) != int:
        print("정수를 입력하세요")

    elif ip < 1 or ip > 3:
        print("1,2,3만 입력가능")
    
    else:
        break