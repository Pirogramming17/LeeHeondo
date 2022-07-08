#함수 이름은 변경 가능합니다.

##############  menu 1
def Menu1(name, mid_score, final_score, students):
    #사전에 학생 정보 저장하는 코딩 
    students.name = name
    students.mid_score = mid_score
    print("Inserted successfully")

##############  menu 2
def Menu2(name, mid_score, final_score, students):
    #학점 부여 하는 코딩
    name = input("Enter name: ")
    if name in students:
        mid_score, final_score = students[name]
        grade = (mid_score + final_score) / 2
        if grade >= 90:
            print(f"{name}'s grade is A")
        elif grade >= 80:
            print(f"{name}'s grade is B")
        elif grade >= 70:
            print(f"{name}'s grade is C")
        else:
            print(f"{name}'s grade is F")
    else:
        print("name does not exist")   

##############  menu 3
def Menu3(name, mid_score, final_score, students):
    #출력 코딩
    for name, [mid_score, final_score] in students.items():
    grade = (mid_score + final_score) / 2
    print(f"{name}'s grade is {grade}")

##############  menu 4
def Menu4(name, mid_score, final_score):
    #학생 정보 삭제하는 코딩
    name = input("Enter name: ")
    if name in students:
        del students[name]
        print("Deleted successfully")
    else:
        print("name does not exist")

#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
class students(name, mid_score, final_score):
    def __init__(self, name, mid_score, final_score):
        self.name = name
        self.mid_score = mid_score
        self.final_score = final_score
        self.grade = (mid_score + final_score) / 2
while True : 
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        #학생 정보 입력받기
        name, mid_score, final_score = map(input("Enter name mid-score final-score: ").slice())
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        try:
            mid_score = int(mid_score)
            final_score = int(final_score)
            if mid_score < 0 or final_score < 0:
                print("Score must be positive integer")
            elif name in students:
                print("name already exists")
            else:
                Menu1(name,mid_score,final_score, students)
        except ValueError:
            print("Score must be positive integer")
    elif choice == "2" :
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우 2번 함수 호출
        #"Grading to all students." 출력
        if students != []:
            Menu2(name,mid_score,final_score)
        else:
            print("No student data!")   

    elif choice == "3" :
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        #예외사항이 아닌 경우 3번 함수 호출
        Menu3(name, mid_score, final_score, students)
    elif choice == "4" :
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력
        name = input("Enter name: ")
        if name in students:
            Menu4(name, mid_score, final_score)
        else:
            print("name does not exist")
    elif choice == "5" :
        #프로그램 종료 메세지 출력
        #반복문 종료
        break
    else :
        #"Wrong number. Choose again." 출력
        print("Wrong number. Choose again.")