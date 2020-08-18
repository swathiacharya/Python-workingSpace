class Student:
    studCount = 0
    def __init__(self,studId = 0, studName = '', phoneNo = '',emailId=''):
        self.studId = studId
        self.studName =studName
        self.phoneNo = phoneNo
        self.emailId = emailId
        Student.studCount +=1
    
    def showCount(self):
        print("count",Student.studCount)
    def showData(self):
        print('studName:   ',self.studName)
        print('studentId:  ',self.studId )
        print('phone       ',self.phoneNo)
        print('email       ',self.emailId)
    # def __del__(self):
    #     class_name = self.__class__.__name__
    #     print(class_name,"destor")
s1 = Student(1,'swathi','+8867946883','acharyaswathi@gmail.com')
s2 = Student(1,'swathi1','+8867946883','acharyaswathi@gmail.com')

s3 = Student(1,'swathi2','+8867946883','acharyaswathi@gmail.com')

print(Student.__doc__)
print(Student.studCount)
Student.showCount(s1)
Student.showData(s1)

if(hasattr(s1,'studName')):
    print(getattr(s1,'studName'))
    
print(Student.__dict__)
print(Student.__doc__)
print(Student.__name__)
print(Student.__module__)
print(Student.__base__)

print()
print()
# print(id(s1))
# print(id(s2))
# print(id(s3))
# del(s1)
# del(s2)
# del(s3)
# del(s1)
# s1.showCount()

class StudentCourse(Student):
    __courseName = ''
    def __init__(self,studId = 0, studName = '', phoneNo = '',emailId='', courseName=''):
        Student.__init__(self,studId = 0, studName = '', phoneNo = '',emailId='')
        self.courseName = courseName
    def showData(self):
        Student.showData(self)
        print(self.courseName)
        
sc3 = StudentCourse(1,'swathi2','+8867946883','acharyaswathi@gmail.com','cse')
print(sc3._StudentCourse__courseName)
sc3.showData()

class Book:
    title =''
    page = 0
    def __init__(self,title='', page = 0):
        self.title = title
        self.page = page
    
    def __str__(self):
        return self.title
    def __radd__(self,other):
        return self.page + other
    def __add__(self,other):
        return self.page + other.page
    def __sub__(self,other):
        return self.page - other.page
    def __mul__(self,other):
        return self.page * other.page
    def __pow__(self,other):
        return self.page ** other.page
    def __truediv__(self,other):
        return self.page / other.page
    
book1 = Book('aa', 2)
book2 = Book('kk', 5)
print(book1 + book2)
print(book1 - book2)
print(book1 * book2)
print(book1 / book2)
print(book1 ** book2)


class Point:
    def __init__(self, x= 0, y = 0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print('del ',class_name)
    def __lt__(self,other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        
        other_mag = (other.x ** 2) + (other.y ** 2)
        print(self_mag,other_mag)
        return self_mag< other_mag

res = Point(1,1) > Point(2,5)

print(res)