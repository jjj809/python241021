# Person 클래스 정의
class Person:
    # 생성자: id와 name을 매개변수로 받아 초기화
    def __init__(self, id, name):
        self.id = id  # id 멤버 변수 초기화
        self.name = name  # name 멤버 변수 초기화
    
    # printInfo 메서드: id와 name을 출력하는 메서드
    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")

# Manager 클래스 정의 (Person 클래스를 상속받음)
class Manager(Person):
    # 생성자: id, name과 추가로 title을 받아 초기화
    def __init__(self, id, name, title):
        # 부모 클래스(Person)의 생성자를 호출하여 id와 name을 초기화
        super().__init__(id, name)
        self.title = title  # title 멤버 변수 초기화
    
    # printInfo 메서드: 부모 클래스의 printInfo 메서드를 호출한 후, title도 출력
    def printInfo(self):
        # 부모 클래스의 printInfo 메서드 호출
        super().printInfo()
        # title 출력 추가
        print(f"Title: {self.title}")

# Employee 클래스 정의 (Person 클래스를 상속받음)
class Employee(Person):
    # 생성자: id, name과 추가로 skill을 받아 초기화
    def __init__(self, id, name, skill):
        # 부모 클래스(Person)의 생성자를 호출하여 id와 name을 초기화
        super().__init__(id, name)
        self.skill = skill  # skill 멤버 변수 초기화
    
    # printInfo 메서드: 부모 클래스의 printInfo 메서드를 호출한 후, skill도 출력
    def printInfo(self):
        # 부모 클래스의 printInfo 메서드 호출
        super().printInfo()
        # skill 출력 추가
        print(f"Skill: {self.skill}")

# 테스트 함수 정의
def run_tests():
    # 1. Person 클래스 테스트 (Alice라는 Person 객체 생성 및 정보 출력)
    p1 = Person(1, "Alice")
    p1.printInfo()  # 출력: ID: 1, Name: Alice
    
    # 2. Person 클래스 테스트 (Bob이라는 Person 객체 생성 및 정보 출력)
    p2 = Person(2, "Bob")
    p2.printInfo()  # 출력: ID: 2, Name: Bob
    
    # 3. Manager 클래스 테스트 (Charlie라는 Manager 객체 생성 및 정보 출력)
    m1 = Manager(3, "Charlie", "Team Leader")
    m1.printInfo()  # 출력: ID: 3, Name: Charlie, Title: Team Leader
    
    # 4. Manager 클래스 테스트 (Dave라는 Manager 객체 생성 및 정보 출력)
    m2 = Manager(4, "Dave", "Director")
    m2.printInfo()  # 출력: ID: 4, Name: Dave, Title: Director
    
    # 5. Employee 클래스 테스트 (Eve라는 Employee 객체 생성 및 정보 출력)
    e1 = Employee(5, "Eve", "Python")
    e1.printInfo()  # 출력: ID: 5, Name: Eve, Skill: Python
    
    # 6. Employee 클래스 테스트 (Frank라는 Employee 객체 생성 및 정보 출력)
    e2 = Employee(6, "Frank", "Java")
    e2.printInfo()  # 출력: ID: 6, Name: Frank, Skill: Java
    
    # 7. 상속 및 오버라이딩 확인 (Grace라는 Manager 객체 생성 및 정보 출력)
    m3 = Manager(7, "Grace", "Project Manager")
    m3.printInfo()  # 출력: ID: 7, Name: Grace, Title: Project Manager
    
    # 8. 상속 및 오버라이딩 확인 (Hank라는 Employee 객체 생성 및 정보 출력)
    e3 = Employee(8, "Hank", "C++")
    e3.printInfo()  # 출력: ID: 8, Name: Hank, Skill: C++
    
    # 9. Person 클래스의 속성 확인 (Ivy라는 Person 객체 생성 후 id와 name 속성 출력)
    p3 = Person(9, "Ivy")
    print(f"p3 ID: {p3.id}, Name: {p3.name}")  # 출력: p3 ID: 9, Name: Ivy
    
    # 10. Employee 클래스의 속성 확인 (Jack이라는 Employee 객체 생성 후 id, name, skill 속성 출력)
    e4 = Employee(10, "Jack", "JavaScript")
    print(f"e4 ID: {e4.id}, Name: {e4.name}, Skill: {e4.skill}")  # 출력: e4 ID: 10, Name: Jack, Skill: JavaScript

# 테스트 실행
run_tests()
