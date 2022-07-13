def Menu1(name, mid_score, final_score,Student,students):
    #사전에 학생 정보 저장하는 코딩 
    name = Student(name, mid_score, final_score)
    students.append(name)

def Menu2(students):
    #학점 부여 하는 코딩
    for i in range(len(students)):
        k = (students[i].mid_score + students[i].final_score) / 2
        if k >= 90:
            students[i].grade = 'A'
        elif k >= 80:
            students[i].grade = 'B'
        elif k >= 70:
            students[i].grade = 'C'
        else:
            students[i].grade = 'F'
    print("Grading to all students")
    
def Menu3(students):
    #출력 코딩
    print("-----------------------------------")
    print("name\tmid\tfinal\tgrade")
    print("-----------------------------------")
    for i in range(len(students)):
        print(f"{students[i].name}\t{students[i].mid_score}\t{students[i].final_score}\t{students[i].grade}")

def Menu4(students,i):

        print(f"{students[i].name} student information is deleted.")
        del students[i]

class Student:
    def __init__(self, name, mid_score, final_score):
        self.name = name
        self.mid_score = mid_score
        self.final_score = final_score
        self.grade = 0

students=[]
while True : 
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        try:
            name, mid_score, final_score = input("Enter name mid-score final-score: ").split()
        except ValueError:
            print("Num of data is not 3!")
            continue
        try:
            mid_score = int(mid_score)
            final_score = int(final_score)
            for i in range(len(students)):
                if name == students[i].name:
                    print("name already exists")
            if mid_score < 0 or final_score < 0:
                print("Score must be positive integer")                  
            else:
                Menu1(name,mid_score,final_score,Student,students)

        except ValueError:
            print("Score must be positive integer")
    elif choice == "2" :
            #예외사항 처리(저장된 학생 정보의 유무)
            #예외사항이 아닌 경우 2번 함수 호출
            #"Grading to all students." 출력
            if students != []:
                Menu2(students)
            else:
                print("No student data!")   

    elif choice == "3" :
        a = True
        if students == []:
            print("No student data!") 
            continue
        for i in range(len(students)):
            if students[i].grade == 0:
                print("There is a student who didn't get grade")
                a = False
                break
        if a:
            Menu3(students)
    elif choice == "4" :
        a = True
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력
        if students != []:
            name = input("Enter name: ")
            for i in range(len(students)):
                if name == students[i].name:
                    a = False
                    Menu4(students,i)
                    #break
            if a:
                print("Not exist name!") 
        else:
            print("No student data!") 
    elif choice == "5" :
        print("Exit Program!")
        break
    else :
        print("Wrong number. Choose again.")

