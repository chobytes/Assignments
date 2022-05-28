class Student:
    def __str__(self) -> str:
        return "Student"

    def printStudent(self) -> None:
        print(self.__str__())

class GraduateStudent(Student):
    def __str__(self) -> str:
        return "Graduate Student"

    def printStudent(self) -> None:
        print(self.__str__())

a = Student()
b = GraduateStudent()
a.printStudent()
b.printStudent()

