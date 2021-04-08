# 类与定义
class Student(object):
    def __init__(self, gender, name, score):
        self.__name = name
        self.__gender = gender
        self.__score = score

    def printmine(self):
        print('%s %s'%(self.__name, self.__score))

    def grade(self):
        if self.__score>90:
            return 'A'
        elif self.__score>60:
            return 'B'
        else:
            return 'C'

    def getname(self):
        return self.__name

    def getgender(self):
        return self.__gender

    def getscore(self):
        return self.__score

    def setscore(self, score):   # 修改私有成员数值的方法
        self.__score = score


s1 = Student('Frank', 'male', 99)
s2 = Student('Aimee', 'female', 61)
s2.setscore(90)
s1.printmine()
print(s1.getname(), s1.getscore(), s1.grade())
print(s2.getname(), s2.getscore(), s2.grade())
